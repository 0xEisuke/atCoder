import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    out = []
    for _ in range(T):
        N, M, K = map(int, input().split())
        S = input().strip()
        adj = [[] for _ in range(N)]
        for _ in range(M):
            u, v = map(int, input().split())
            adj[u-1].append(v-1)

        dp = [c == 'A' for c in S]

        for r in range(1, 2*K + 1):
            nxt = [False]*N
            if r & 1:
                for u in range(N):
                    ok = True
                    for v in adj[u]:
                        if not dp[v]:
                            ok = False
                            break
                    nxt[u] = ok
            else:
                for u in range(N):
                    ok = False
                    for v in adj[u]:
                        if dp[v]:
                            ok = True
                            break
                    nxt[u] = ok
            dp = nxt

        out.append("Alice" if dp[0] else "Bob")

    print("\n".join(out))

if __name__ == "__main__":
    main()
