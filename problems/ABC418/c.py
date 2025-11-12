import sys
import bisect
input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    total = [0] * (n + 1)
    for i in range(n):
        total[i + 1] = total[i] + arr[i]
    max_a = arr[-1]

    for _ in range(q):
        b = int(input())
        if b > max_a:
            print(-1)
            continue
        pos = bisect.bisect_left(arr, b - 1)
        # print("pos:", pos)
        # print("arr:", arr[pos:])
        count = total[pos] + (n - pos) * (b - 1) + 1
        # print("total:", total[pos])
        # print("count:", count)
        print(count)

if __name__ == "__main__":
    main()
