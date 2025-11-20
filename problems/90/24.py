import sys

def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    c = [abs(a[i] - b[i]) for i in range(n)]
    total = sum(c)
    if (total - k) % 2 == 0 and total <= k:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()