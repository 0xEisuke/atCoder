import sys
from math import gcd
from collections import defaultdict

def norm_slope(dx, dy):
    if dx == 0:
        return (0, 1)
    if dy == 0:
        return (1, 0)
    g = gcd(abs(dx), abs(dy))
    dx //= g; dy //= g
    if dx < 0:
        dx = -dx; dy = -dy
    return (dx, dy)

def main():
    input = sys.stdin.readline
    n = int(input())
    P = [tuple(map(int, input().split())) for _ in range(n)]

    slope_cnt = defaultdict(int)
    mid_cnt   = defaultdict(int)

    for i in range(n):
        x1, y1 = P[i]
        for j in range(i+1, n):
            x2, y2 = P[j]
            dx = x2 - x1
            dy = y2 - y1
            slope = norm_slope(dx, dy)
            slope_cnt[slope] += 1
            mid = (x1 + x2, y1 + y2)
            mid_cnt[mid] += 1

    total_by_slope = 0
    for m in slope_cnt.values():
        total_by_slope += m * (m - 1) // 2

    parallelograms = 0
    for k in mid_cnt.values():
        parallelograms += k * (k - 1) // 2

    ans = total_by_slope - parallelograms
    print(ans)

if __name__ == "__main__":
    main()
