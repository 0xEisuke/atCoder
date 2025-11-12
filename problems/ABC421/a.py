import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    rooms = []
    for _ in range(n):
        s = input().strip()
        rooms.append(s)

    x, y = input().split()
    x = int(x)

    if rooms[x - 1] == y:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
