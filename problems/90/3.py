# # 木の直径、DFS

# 「グラフの2頂点間の距離の最大値」のことを、そのグラフの直径と言う

# 木の直径は次の方法で求められる (証明は略)。
# 1,適当な頂点uを1つ選ぶ
# 2,頂点uから最も遠い頂点vを求める (O(N))
# 3,頂点 vから最も遠い頂点wを求める (O(N))
# このとき、パスv-wの長さが求める直径になる

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def dfs(s,G,N):
    dist = [-1] * N
    dist[s] = 0
    stack = deque([s])
    
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                stack.append(nv)
    
    return dist

def main():
    N = int(input())
    G = defaultdict(list)
    for _ in range(N-1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    
    dist0 = dfs(0,G,N)
    mv = max(enumerate(dist0), key=lambda x: x[1])[0]
    distmv = dfs(mv,G,N)
    print(max(distmv)+1)

if __name__ == "__main__":
    main()