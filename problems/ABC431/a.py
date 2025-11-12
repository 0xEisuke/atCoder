import sys

def main():
    input = sys.stdin.readline
    h,b = map(int, input().split())
    if h < b:
        print(0)
    else:
        print(h - b)

if __name__ == "__main__":
    main()
