import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    a, b, c = lst

    INF = 10**18
    ans = INF

    LIMIT = 10000

    for i in range(LIMIT + 1):
        sum_a = a * i
        if sum_a > n:
            break

        max_j = min(LIMIT - i, (n - sum_a) // b)

        for j in range(max_j + 1):
            sum_ab = sum_a + b * j
            rem = n - sum_ab
            if rem < 0:
                break

            if rem % c == 0:
                k = rem // c
                coins = i + j + k
                if coins < ans:
                    ans = coins

    print(ans)

if __name__ == "__main__":
    main()
