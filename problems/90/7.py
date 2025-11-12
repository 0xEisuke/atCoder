# 二分探索で解く
# bisect module を使うと楽

import sys
import bisect
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    Q = int(input())
    for _ in range(Q):
        B = int(input())
        i = bisect.bisect_left(A, B)

        if i < N and A[i] == B:
            print(0)
            continue

        cand = []
        if i > 0:      # 左側の要素がある
            cand.append(B - A[i-1])
        if i < N:      # 右側の要素がある
            cand.append(A[i] - B)

        print(min(cand))

if __name__ == "__main__":
    main()
