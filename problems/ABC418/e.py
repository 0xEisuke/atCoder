import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    points.sort()
    
    # [{slope,((xi,yi),(x2,y2)),((xi,yi),(x2,y2))}]のように傾きとその傾きになる２点のペアの集合を記録
    slopes = {} # 傾きをキーにしてペアのリストを値とする辞書

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            slope = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
            if slope not in slopes:
                slopes[slope] = []
            slopes[slope].append((points[i], points[j]))
    
    # 各傾きに対してペアの数を数える
    total = 0
    for slope, pairs in slopes.items():
        total += len(pairs) * (len(pairs) - 1) // 2

    print(total)
    
    
if __name__ == "__main__":
    main()