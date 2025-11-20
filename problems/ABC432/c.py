import sys
from math import gcd

input = sys.stdin.readline

def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    D = y - x  # > 0
    g = gcd(x, D)
    M = D // g

    base = a[0] % M
    for v in a:
        if v % M != base:
            print(-1)
            return

    low = max(x * v for v in a)
    high = min(y * v for v in a)
    if low > high:
        print(-1)
        return

    r = (x * a[0]) % D
    W = high - ((high - r) % D)
    if W < low:
        print(-1)
        return

    totalA = sum(a)
    ans = (n * W - x * totalA) // D
    print(ans)

if __name__ == "__main__":
    main()
