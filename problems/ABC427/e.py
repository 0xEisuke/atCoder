import sys

from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def main():
    input = sys.stdin.readline
    H,W = map(int,input().split())
    grid = []
    posOfT = (0,0)
    for i in range(H):
        S = input().strip()
        if "T" in S:
            posOfT = (i,S.index("T"))
        lstS = list(S)
        grid.append(lstS)
    # print(grid)
    
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    uf = UnionFind(H*W + 1)
    # print(uf.parents)
    
    for dx,dy in dir:
        ni = posOfT[0] + dx
        nj = posOfT[1] + dy
        if 0 <= ni < H and 0 <= nj < W:
            if grid[ni][nj] == ".":
                uf.union(posOfT[0]*W+posOfT[1],ni*W+nj)
        elif ni < 0 or ni >= H or nj < 0 or nj >= W:
            uf.union(posOfT[0]*W+posOfT[1],H*W)
    
    for i in range(H):
        for j in range(W):
            for dx,dy in dir:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < H and 0 <= nj < W:
                    if grid[i][j] == "." and grid[ni][nj] == ".":
                        uf.union(i*W+j,ni*W+nj)
                    # elif grid[i][j] == "." and grid[ni][nj] == "T":
                    #     uf.union(i*W+j,ni*W+nj)
                    # elif grid[i][j] == "T" and grid[ni][nj] == ".":
                    #     uf.union(i*W+j,ni*W+nj)
                    # else:
                    #     continue
                if i == 0 or j == 0 or i == H-1 or j == W-1:
                    if grid[i][j] == ".":
                        uf.union(i*W+j,H*W)
    
    
    print(uf.same(posOfT[0]*W+posOfT[1],H*W))

if __name__ == "__main__":
    main()