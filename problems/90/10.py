# クラスごとに累積和を取って、区間和を高速に求める

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    S1 = [0] * (N + 1)
    S2 = [0] * (N + 1)

    for i in range(1, N + 1):
        c, p = map(int, input().split())
        S1[i] = S1[i-1] + (p if c == 1 else 0)
        S2[i] = S2[i-1] + (p if c == 2 else 0)

    Q = int(input())
    out = []
    for _ in range(Q):
        L, R = map(int, input().split())
        sum1 = S1[R] - S1[L-1]
        sum2 = S2[R] - S2[L-1]
        out.append(f"{sum1} {sum2}")

    print("\n".join(out))

if __name__ == "__main__":
    main()
