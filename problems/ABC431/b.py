import sys

def main():
    input = sys.stdin.readline
    x = int(input())
    n = int(input())
    w_lst = list(map(int, input().split()))
    q = int(input())
    total = x
    parts = []
    for _ in range(q):
        p = int(input())
        if p in parts:
            total -= w_lst[p - 1]
            parts.remove(p)
        else:
            total += w_lst[p - 1]
            parts.append(p)
        print(total)
        

if __name__ == "__main__":
    main()
