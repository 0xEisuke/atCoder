import sys
input = sys.stdin.readline

def main():
    N,Y = map(int,input().split())
    
    if Y % 1000 != 0:
        print(-1, -1, -1)
        return
    
    flag = False
    
    max_10000 = min(N, Y // 10000)
    for i in range(max_10000 + 1):
        
        rest1 = Y - i*10_000
        max_5000 = min(N - i, rest1 // 5000)
        for j in range(max_5000 + 1):
            cnt = i+j
            rest2 = rest1 - j*5000
            k = rest2 // 1000
            cnt += k
            if cnt == N:
                print(i,j,k)
                flag = True
                return
    
    if not flag:
        print(-1,-1,-1)
    
if __name__ == "__main__":
    main()