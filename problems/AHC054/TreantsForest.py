# Treant's Forest - Far-Loop Strategy (Robust I/O & Anti-Confirmed-Placement)
# Python 3.x

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

DIR4 = [(-1,0),(0,-1),(0,1),(1,0)]  # U,L,R,D

def inb(i,j,N):
    return 0 <= i < N and 0 <= j < N

def bfs_dist_and_parent(grid, N, si, sj, ti, tj):
    dist = [[-1]*N for _ in range(N)]
    par  = [[None]*N for _ in range(N)]
    dq = deque()
    dist[si][sj] = 0
    dq.append((si,sj))
    while dq:
        i,j = dq.popleft()
        if (i,j) == (ti,tj): break
        for di,dj in DIR4:
            ni, nj = i+di, j+dj
            if inb(ni,nj,N) and grid[ni][nj]=='.' and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                par[ni][nj]  = (i,j)
                dq.append((ni,nj))
    return dist, par

def reconstruct_path(par, ti, tj):
    if par[ti][tj] is None:
        return []
    cur = (ti,tj)
    path = [cur]
    while par[cur[0]][cur[1]] is not None:
        cur = par[cur[0]][cur[1]]
        path.append(cur)
    path.reverse()
    return path

def still_connected_after(grid, N, src, dst, tentative_blocks):
    # 仮に木にしてから入口->花の到達性をチェック
    changed = []
    for (i,j) in tentative_blocks:
        if grid[i][j] == '.':
            grid[i][j] = 'T'
            changed.append((i,j))
    dist, _ = bfs_dist_and_parent(grid, N, src[0], src[1], dst[0], dst[1])
    ok = (dist[dst[0]][dst[1]] != -1)
    for (i,j) in changed:
        grid[i][j] = '.'
    return ok

def make_ring_candidates(N, ti, tj, R):
    # マンハッタン距離 R の簡易リング候補（北・南にゲート）
    cand = []
    for i in range(N):
        for j in range(N):
            if abs(i-ti) + abs(j-tj) == R:
                cand.append((i,j))
    gates = set()
    if cand:
        g1 = min(cand, key=lambda x:(x[0], x[1]))    # 北（最上）
        g2 = max(cand, key=lambda x:(x[0], -x[1]))   # 南（最下）
        gates.add(g1); gates.add(g2)
    return [c for c in cand if c not in gates]

def read_until_k_ints(initial_tokens, need):
    """initial_tokens を先頭に、必要数 need 個の整数が集まるまで行を読み足す"""
    out = []
    for t in initial_tokens:
        if t != '':
            out.append(int(t))
    while len(out) < need:
        line = input()
        if not line:
            break
        for t in line.split():
            if t != '':
                out.append(int(t))
                if len(out) == need:
                    break
    return out

def main():
    # 初期入力
    first = input().split()
    if not first:
        return
    N, ti, tj = map(int, first)
    grid = [list(input()) for _ in range(N)]

    revealed = [[False]*N for _ in range(N)]
    start = (0, N//2)
    # 入口は初期から確認済み（仕様上、最初のターンで与えられるが安全のため先にTrue）
    if inb(start[0], start[1], N):
        revealed[start[0]][start[1]] = True

    # 戦略パラメータ
    MAX_PER_TURN = 2
    RING_R = max(3, N//6)
    ring_cands = make_ring_candidates(N, ti, tj, RING_R)

    while True:
        line = input()
        if not line:
            # 入力枯渇時は打ち切り
            print("-1")
            sys.stdout.flush()
            return
        parts = line.split()
        if len(parts) < 2:
            print("-1")
            sys.stdout.flush()
            return

        pi, pj = map(int, parts[:2])

        # 花に到達したら、n 行を読まず終了
        if pi == ti and pj == tj:
            break

        # n と 2n 個の座標を堅牢に読み切る
        line2 = input()
        if not line2:
            print("-1")
            sys.stdout.flush()
            return
        p2 = line2.split()
        if not p2:
            print("-1")
            sys.stdout.flush()
            return

        n = int(p2[0])
        need = 2 * n
        # 同じ行に座標が続いている場合はそれも含めて収集、足りなければ次行以降で補完
        xy = read_until_k_ints(p2[1:], need)

        # ★ ここが重要：2n 個すべて揃ってから revealed を更新 ★
        if len(xy) < need:
            # 形式異常だが、安全に打ち切る
            print("-1")
            sys.stdout.flush()
            return

        # ★ 現在位置を必ず確認済みにする
        if inb(pi, pj, N):
            revealed[pi][pj] = True

        for k in range(n):
            x = xy[2*k]
            y = xy[2*k+1]
            if inb(x,y,N):
                revealed[x][y] = True

        # --- 配置計算（確認済みセルには絶対置かない） ---
        placed = []

        # 1) リング候補から
        if ring_cands:
            nxt = []
            for (ri,rj) in ring_cands:
                if len(placed) >= MAX_PER_TURN:
                    nxt.append((ri,rj))
                    continue
                # 多重ガード：境界内・未確認・空き
                if not inb(ri,rj,N): 
                    continue
                if revealed[ri][rj]: 
                    continue
                if grid[ri][rj] != '.': 
                    continue
                if still_connected_after(grid, N, start, (ti,tj), [(ri,rj)]):
                    grid[ri][rj] = 'T'
                    placed.append((ri,rj))
                else:
                    nxt.append((ri,rj))
            # 候補の再フィルタ（すでに木化/確認済みになったものを落とす）
            ring_cands = [c for c in nxt if inb(c[0],c[1],N) and grid[c[0]][c[1]] == '.' and not revealed[c[0]][c[1]]]

        # 2) 最短路上の未確認セルを塞いで遠回り
        if len(placed) < MAX_PER_TURN:
            dist, par = bfs_dist_and_parent(grid, N, pi, pj, ti, tj)
            if dist[ti][tj] != -1:
                path = reconstruct_path(par, ti, tj)
                for (ci,cj) in reversed(path):
                    if len(placed) >= MAX_PER_TURN:
                        break
                    if (ci,cj) == (pi,pj) or (ci,cj) == (ti,tj):
                        continue
                    # 多重ガード：空き・未確認のみ
                    if grid[ci][cj] != '.': 
                        continue
                    if revealed[ci][cj]: 
                        continue
                    if still_connected_after(grid, N, start, (ti,tj), [(ci,cj)]):
                        grid[ci][cj] = 'T'
                        placed.append((ci,cj))

        # 出力
        if not placed:
            print(0, flush=True)
        else:
            out = [str(len(placed))]
            for (x,y) in placed:
                out += [str(x), str(y)]
            print(" ".join(out), flush=True)

if __name__ == "__main__":
    main()
