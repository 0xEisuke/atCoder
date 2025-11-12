import sys
import math
from bisect import bisect_left

input = sys.stdin.readline

def main():
    N = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    PI = math.pi
    TWO_PI = 2 * math.pi
    best = 0.0  # 最大角（ラジアン）

    for i in range(N):
        xi, yi = pts[i]
        angs = []
        for j in range(N):
            if i == j:
                continue
            xj, yj = pts[j]
            angs.append(math.atan2(yj - yi, xj - xi))
        angs.sort()

        # wrap 用に +2π を付け足す
        ext = angs + [a + TWO_PI for a in angs]

        m = len(angs)
        for a in angs:
            target = a + PI  # 180度に近い相手を探す
            k = bisect_left(ext, target)

            # 近い候補は ext[k-1], ext[k]
            for t in (ext[k - 1], ext[k] if k < len(ext) else ext[-1]):
                diff = abs(t - a)
                if diff > PI:
                    diff = TWO_PI - diff  # 角度差は最大でもπ
                if diff > best:
                    best = diff

    print("{}".format(math.degrees(best)))

if __name__ == "__main__":
    main()
