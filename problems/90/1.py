# 二分探索

import sys

def check(mid, A, K, L):
    cnt = 0
    pre = 0
    for a in A:
        if a - pre >= mid:
            cnt += 1
            pre = a
    if L - pre >= mid:
        cnt += 1
    return cnt >= K+1

def main():
    input = sys.stdin.readline
    
    N,L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    
    left, right = -1, L+1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid, A, K, L):
            left = mid
        else:
            right = mid

    print(left)

if __name__ == "__main__":
    main()