import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    lst = []
    for _ in range(N):
        d = int(input())
        lst.append(d)
    
    print(len(set(lst)))

if __name__ == "__main__":
    main()