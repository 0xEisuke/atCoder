# bit全探索

import sys
from itertools import product
input = sys.stdin.readline

def check(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    
    return (cnt == 0)

def main():
    N = int(input())
    
    for s in product(["(",")"],repeat=N):
        if check(s):
            print(*s, sep="")

if __name__ == "__main__":
    main()