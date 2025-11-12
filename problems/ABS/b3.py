import sys
input = sys.stdin.readline

def main():
    N,A,B = map(int,input().split())
    cnt = 0
    lst = []
    
    for i in range(1,N+1):
        j = i 
        s = 0
        while i > 0:
            mod = i % 10
            i //= 10
            s += mod
        if A <= s <= B:
            cnt += j
            lst.append(j)
            
    
    # print(*lst)
    print(cnt)

if __name__ == "__main__":
    main()