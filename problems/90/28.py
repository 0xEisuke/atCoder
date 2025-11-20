import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    area = [[0] * 1000 for _ in range(1001)]
    for _ in range(n):
        lx, ly, rx, ry = map(int, input().split())
        for y in range(ly, ry):
            area[lx][y] += 1
            area[rx][y] -= 1
    for x in range(1, 1000):
        for y in range(1000):
            area[x][y] += area[x-1][y]
    
    cnt = [0] * (n + 1)
    for x in range(1000):
        for y in range(1000):
            v = area[x][y]
            if 1 <= v <= n:
                cnt[v] += 1

    for i in range(1, n + 1):
        print(cnt[i])


if __name__ == "__main__":
    main()