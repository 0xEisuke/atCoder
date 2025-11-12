import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    # while True:
    #     for i in range(N):
    #         if lst[i] % 2 != 0:
    #             print(cnt)
    #             return
    #         lst[i] //= 2
    #     cnt += 1
    while all(x % 2 == 0 for x in lst):
        lst = [x // 2 for x in lst]
        cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()
