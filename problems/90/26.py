import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    color = [-1] * n  # 0 or 1
    q = deque([0])
    color[0] = 0

    while q:
        v = q.popleft()
        for to in graph[v]:
            if color[to] == -1:
                color[to] = 1 - color[v]
                q.append(to)

    group0 = [i + 1 for i in range(n) if color[i] == 0]
    group1 = [i + 1 for i in range(n) if color[i] == 1]

    if len(group0) >= n // 2:
        print(*group0[: n // 2])
    else:
        print(*group1[: n // 2])

if __name__ == "__main__":
    main()
