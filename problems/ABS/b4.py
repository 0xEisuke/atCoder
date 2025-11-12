import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    lst = list(map(int,input().split()))
    
    lst.sort(reverse=True)
    # print(lst)
    
    alice = sum(lst[::2])
    bob = sum (lst[1::2])
    print(alice - bob)

if __name__ == "__main__":
    main()