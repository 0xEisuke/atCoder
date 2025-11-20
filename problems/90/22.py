import sys
import math

def main():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    g = math.gcd(A, math.gcd(B, C))
    ans = A // g + B // g + C // g - 3
    print(ans)

if __name__ == "__main__":
    main()
