import sys

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    H = list(map(int, input().split()))
    B = list(map(int, input().split()))

    H.sort()
    B.sort()

    i = 0
    j = 0
    cnt = 0

    while i < N and j < M and cnt < K:
        if B[j] < H[i]:
            j += 1
        else:
            cnt += 1
            i += 1
            j += 1

    print("Yes" if cnt >= K else "No")

if __name__ == "__main__":
    main()
