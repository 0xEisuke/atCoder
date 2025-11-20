import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    usernames = set()
    for i in range(n):
        s = input().strip()
        if s not in usernames:
            print(i+1)
        usernames.add(s)

if __name__ == "__main__":
    main()