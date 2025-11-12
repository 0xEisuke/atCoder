import sys

def main():
    input = sys.stdin.readline
    s = input().strip()
    lst = list(map(int,s))
    print(sum(1 for x in lst if x == 1))

if __name__ == "__main__":
    main()