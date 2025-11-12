import sys
from collections import deque

INF = 10**9
# d: 0=up,1=right,2=down,3=left
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

map_out = {
    'A': {0:0, 1:1, 2:2, 3:3},
    'B': {0:3, 1:2, 2:1, 3:0},
    'C': {0:1, 1:0, 2:3, 3:2}
}

def solve_case(H, W, S):
    dist = [[[INF]*4 for _ in range(W)] for __ in range(H)]
    dq = deque()
    start_i, start_j, start_d = 0, 0, 1
    dist[start_i][start_j][start_d] = 0
    dq.append((start_i, start_j, start_d))

    while dq:
        i, j, d = dq.popleft()
        cur = dist[i][j][d]
        for t in ('A','B','C'):
            out_d = map_out[t][d]
            ni = i + di[out_d]
            nj = j + dj[out_d]
            cost = 0 if S[i][j] == t else 1
            new_cost = cur + cost
            if 0 <= ni < H and 0 <= nj < W:
                if new_cost < dist[ni][nj][out_d]:
                    dist[ni][nj][out_d] = new_cost
                    if cost == 0:
                        dq.appendleft((ni, nj, out_d))
                    else:
                        dq.append((ni, nj, out_d))
    ans = INF
    for i in range(H):
        for j in range(W):
            for d in range(4):
                cur = dist[i][j][d]
                if cur == INF:
                    continue
                for t in ('A','B','C'):
                    out_d = map_out[t][d]
                    ni = i + di[out_d]
                    nj = j + dj[out_d]
                    if ni == H-1 and nj == W:
                        add = 0 if S[i][j] == t else 1
                        ans = min(ans, cur + add)
    if ans == INF:
        return -1
    return ans

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    out_lines = []
    for _ in range(T):
        parts = input().split()
        while len(parts) == 0:
            parts = input().split()
        H, W = map(int, parts)
        S = [input().strip() for _ in range(H)]
        res = solve_case(H, W, S)
        out_lines.append(str(res))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
