import sys

def main():
    input = sys.stdin.readline
    a = int(input())
    b,c = map(int,input().split())
    s = input().strip()
    
    print(a+b+c)
    print(s)

if __name__ == "__main__":
    main()