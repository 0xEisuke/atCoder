import sys
from collections import defaultdict

sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    N, X, Y = map(int, input().split())
    ops = []
    for _ in range(N):
        c, a, b = input().split()
        a = int(a)
        b = int(b)
        ops.append((c, a, b))

    rects = [(0, X - 1, 0, Y - 1)]

    for C, A, B in ops:
        new_rects = []
        if C == 'X':
            for x1, x2, y1, y2 in rects:
                if x2 < A:
                    # 全部 x < A → y -> y - B
                    new_rects.append((x1, x2, y1 - B, y2 - B))
                elif x1 >= A:
                    # 全部 x >= A → y -> y + B
                    new_rects.append((x1, x2, y1 + B, y2 + B))
                else:
                    # 境界分割
                    if x1 <= A - 1:
                        new_rects.append((x1, A - 1, y1 - B, y2 - B))
                    new_rects.append((A, x2, y1 + B, y2 + B))
        else:  # C == 'Y'
            for x1, x2, y1, y2 in rects:
                if y2 < A:
                    # 全部 y < A → x -> x - B
                    new_rects.append((x1 - B, x2 - B, y1, y2))
                elif y1 >= A:
                    # 全部 y >= A → x -> x + B
                    new_rects.append((x1 + B, x2 + B, y1, y2))
                else:
                    # 境界分割
                    if y1 <= A - 1:
                        new_rects.append((x1 - B, x2 - B, y1, A - 1))
                    new_rects.append((x1 + B, x2 + B, A, y2))
        rects = new_rects

    m = len(rects)
    # Union-Find
    parent = list(range(m))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        parent[rb] = ra

    right = defaultdict(list)
    left = defaultdict(list)
    top = defaultdict(list)
    bottom = defaultdict(list)
    area = [0] * m

    for idx, (x1, x2, y1, y2) in enumerate(rects):
        area[idx] = (x2 - x1 + 1) * (y2 - y1 + 1)
        right[x2].append((y1, y2, idx))
        left[x1].append((y1, y2, idx))
        top[y2].append((x1, x2, idx))
        bottom[y1].append((x1, x2, idx))

    xs = set(right.keys()) | {x - 1 for x in left.keys()}
    for x in xs:
        R = right.get(x, [])
        L = left.get(x + 1, [])
        if not R or not L:
            continue
        R.sort()
        L.sort()
        i = j = 0
        while i < len(R) and j < len(L):
            y1a, y2a, ida = R[i]
            y1b, y2b, idb = L[j]
            if y2a < y1b:
                i += 1
            elif y2b < y1a:
                j += 1
            else:
                union(ida, idb)
                if y2a <= y2b:
                    i += 1
                else:
                    j += 1

    ys = set(top.keys()) | {y - 1 for y in bottom.keys()}
    for y in ys:
        T = top.get(y, [])
        B = bottom.get(y + 1, [])
        if not T or not B:
            continue
        T.sort()
        B.sort()
        i = j = 0
        while i < len(T) and j < len(B):
            x1a, x2a, ida = T[i]
            x1b, x2b, idb = B[j]
            if x2a < x1b:
                i += 1
            elif x2b < x1a:
                j += 1
            else:
                union(ida, idb)
                if x2a <= x2b:
                    i += 1
                else:
                    j += 1

    comp_area = defaultdict(int)
    for i in range(m):
        comp_area[find(i)] += area[i]

    ans = sorted(comp_area.values())
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    main()
