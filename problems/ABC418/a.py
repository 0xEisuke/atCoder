import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    s = input().strip()

    if s[-3:] == "tea":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()