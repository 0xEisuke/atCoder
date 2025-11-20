# 強連結成分 Strongly Connected Components (SCC) を求める
# 「x から y にも行けて、y から x にも行ける頂点ペア (x, y) の数」はSCCごとの頂点ペアの数
# SCCの各成分の頂点数を k とすると、その成分内の頂点ペア数は kC2 = k*(k-1)/2 で求まる
# 1 回の全体探索で「強連結成分」までまとめてしまうアルゴリズム（SCC分解） を使う
# 解法：Kosaraju のアルゴリズム（DFS 2回）で SCC を求める
# https://chatgpt.com/c/691b293d-3598-8322-9d28-bf8f76f58b1f

import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]   # 元グラフ
    R = [[] for _ in range(N)]   # 逆グラフ（辺の向きだけ反転）

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1  # 0-index にそろえる
        b -= 1
        G[a].append(b)
        R[b].append(a)

    # 1回目のDFS: 帰りがけ順を記録
    visited = [False] * N
    order = []

    def dfs(v):
        visited[v] = True
        for to in G[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for v in range(N):
        if not visited[v]:
            dfs(v)

    # 2回目のDFS: 逆グラフ上で成分IDを振る
    comp = [-1] * N  # 各頂点が属するSCC ID
    cid = 0

    def rdfs(v, cid):
        comp[v] = cid
        for to in R[v]:
            if comp[to] == -1:
                rdfs(to, cid)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid)
            cid += 1

    # 各SCCのサイズを数える
    size = [0] * cid
    for v in range(N):
        size[comp[v]] += 1

    # 各SCC内の頂点ペア数 = kC2 = k*(k-1)/2 を全部足す
    ans = 0
    for k in size:
        ans += k * (k - 1) // 2

    print(ans)

if __name__ == "__main__":
    main()
