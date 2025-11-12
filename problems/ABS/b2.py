import sys
input = sys.stdin.readline

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    
    if X % 50 != 0:
        print(0)
    
    cnt = 0
    maxA = min(X // 500, A)
    
    for i in range(maxA+1):
        rest1 = X - 500*i
        maxB = min(rest1 // 100, B)
        for j in range(maxB+1):
            rest2 = rest1 - 100*j
            if rest2 <= 50*C:
                cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()