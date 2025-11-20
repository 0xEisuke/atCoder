import sys
import math

def main():
    input = sys.stdin.readline
    t = int(input())
    l,x,y = map(int, input().split())
    q = int(input())
    
    for _ in range(q):
        e = int(input())
        theta = 2 * math.pi * e / t
        loc = [0, - (l/2) * math.sin(theta), l/2 - (l/2) * math.cos(theta)]
        
        diff_xy = math.sqrt((loc[0] - x) ** 2 + (loc[1] - y) ** 2)
        diff_z = loc[2]
        angle = math.atan2(diff_z, diff_xy)
        print(math.degrees(angle))

if __name__ == "__main__":
    main()