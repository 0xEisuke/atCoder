import sys

def main():
    input = sys.stdin.readline
    h,w = map(int, input().split())
    if h == 1 or w == 1:
        print(h * w)
        return
    half_h = (h + 1) // 2
    half_w = (w + 1) // 2
    ans = half_h * half_w
    print(ans)

if __name__ == "__main__":
    main()