import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    t = input().strip()

    cnt = [0, 0]

    ones_parity = 0
    for k in range(n + 1):
        key = (ones_parity - k) & 1
        cnt[key] += 1
        if k < n and t[k] == '1':
            ones_parity ^= 1

    ans = cnt[0] * (cnt[0] - 1) // 2 + cnt[1] * (cnt[1] - 1) // 2
    print(ans)

if __name__ == "__main__":
    main()
