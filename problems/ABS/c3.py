import sys
input = sys.stdin.readline

def main():
    N = int(input())
    path = [(0, 0, 0)]
    for _ in range(N):
        t, x, y = map(int, input().split())
        path.append((t, x, y))

    for i in range(N):
        t1, x1, y1 = path[i]
        t2, x2, y2 = path[i+1]
        dt = t2 - t1
        dist = abs(x2 - x1) + abs(y2 - y1)
        if dt < dist or (dt - dist) % 2 != 0:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()
