# union-find を用いた解法
# tle対策として、UnionFindクラスを以下のように少し改造している
# ・最初に要素数を指定しない (H*W が大きすぎるため,Q個が上限の赤マスを動的に要素を追加する方式に)
# ・要素を追加するたびに add メソッドを呼び出し

import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self):
        self.parents = []
    
    def add(self) -> int:
        self.parents.append(-1)
        return len(self.parents) - 1

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

        if self.parents[x] > self.parents[y]: # yの要素数のほうが多い
            x, y = y, x # 入れ替えてxを大きいほうにする

        self.parents[x] += self.parents[y] # xの要素数を更新
        self.parents[y] = x # yの親をxにする

def key(r, c, W):
    # 0-index にして 1 つの整数キーに
    return r * W + c

def main():
    H, W = map(int, input().split())
    Q = int(input())
    
    uf = UnionFind()
    red = set()
    id_of = {}
    out = []
    
    for _ in range(Q):
        qu = list(map(int, input().split()))
        if qu[0] == 1:
            r, c = qu[1]-1, qu[2]-1
            k = key(r, c, W)
            if k in red:
                continue
            red.add(k)
            cur = uf.add()
            id_of[k] = cur
            # 4 近傍
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < H and 0 <= nc < W:
                    nk = key(nr, nc, W)
                    if nk in red:
                        uf.union(cur, id_of[nk])

        else:  # qu[0] == 2
            ra, ca, rb, cb = qu[1]-1, qu[2]-1, qu[3]-1, qu[4]-1
            ka = key(ra, ca, W)
            kb = key(rb, cb, W)

            if not (ka in red and kb in red):
                out.append("No")
            elif uf.find(id_of[ka]) == uf.find(id_of[kb]):
                out.append("Yes")
            else:
                out.append("No")

    print("\n".join(out))

if __name__ == "__main__":
    main()
