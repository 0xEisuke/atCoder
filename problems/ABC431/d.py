import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    W = []
    H = []
    B = []
    total_W = 0
    sum_B = 0
    for _ in range(N):
        wi, hi, bi = map(int, input().split())
        W.append(wi)
        H.append(hi)
        B.append(bi)
        total_W += wi
        sum_B += bi

    C = total_W // 2
    NEG = -10**18
    dp = [NEG] * (C + 1)
    dp[0] = 0

    for i in range(N):
        wi = W[i]
        delta = H[i] - B[i]
        if wi <= C:
            for w in range(C, wi - 1, -1):
                val = dp[w - wi] + delta
                if val > dp[w]:
                    dp[w] = val

    best_extra = max(dp)
    answer = sum_B + best_extra
    print(answer)

if __name__ == "__main__":
    main()
