import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    s = input().strip()

    posA = [i + 1 for i, ch in enumerate(s) if ch == 'A']

    target1 = [2*i + 1 for i in range(n)]
    target2 = [2*(i + 1) for i in range(n)]

    ans1 = sum(abs(a - b) for a, b in zip(posA, target1))
    ans2 = sum(abs(a - b) for a, b in zip(posA, target2))

    print(min(ans1, ans2))

if __name__ == "__main__":
    main()
