# DP で解く典型問題

import sys
input = sys.stdin.readline

MOD = 10**9 + 7

def add(a, b):
    a += b
    if a >= MOD:
        a -= MOD
    return a

def main():
    N = int(input())
    S = input().strip()
    target = "atcoder"

    dp = [[0] * (len(target) + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(len(target) + 1):
            # S[i] を使わない場合
            dp[i + 1][j] = add(dp[i + 1][j], dp[i][j])
            # S[i] を使う場合
            if j < len(target) and S[i] == target[j]:
                dp[i + 1][j + 1] = add(dp[i + 1][j + 1], dp[i][j])

    print(dp[N][len(target)])

if __name__ == "__main__":
    main()