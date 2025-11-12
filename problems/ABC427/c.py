import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    edges = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]

    max_keep = 0
    for mask in range(1 << N):
        cnt = 0
        for u, v in edges:
            if ((mask >> u) & 1) != ((mask >> v) & 1):
                cnt += 1
        if cnt > max_keep:
            max_keep = cnt

    print(M - max_keep)

if __name__ == "__main__":
    main()
