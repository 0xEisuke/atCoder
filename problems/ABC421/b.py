import sys

def rev_fibo(i_1,i_2):
    next = i_1 + i_2
    rev_next = int(str(next)[::-1])
    return(i_2, rev_next)

def main():
    input = sys.stdin.readline
    x,y = map(int, input().split())
    for _ in range(8):
        x,y = rev_fibo(x,y)
    print(y)

if __name__ == "__main__":
    main()