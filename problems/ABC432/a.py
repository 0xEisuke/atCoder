import sys
input = sys.stdin.readline

def main():
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst[0] + lst[1]*10 + lst[2]*100)

if __name__ == "__main__":
    main()