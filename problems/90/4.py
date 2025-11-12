# lambdaの使い方；lambda 引数: 戻り値の式

# zip, *listについて
# １，*lists（アンパック）

# lists = [[2,3,4], [1,5,6], [7,8,9]] のような「リストのリスト」を
# zip([2,3,4], [1,5,6], [7,8,9]) の形に展開する記法。
# * が無いと zip(lists) になって「外側の要素（=内側のリスト）」同士を1つのタプルにしてしまうので目的とズレる。

# ２，zip(...)

# 同じインデックスの要素を“縦方向”に束ねるイテレータを作る。
# 上の例なら
# zip([2,3,4], [1,5,6], [7,8,9]) → (2,1,7), (3,5,8), (4,6,9) を順に生成。

# 重要：zip は最短の長さに合わせて止まる（長さ不一致のときに余りは無視）。


import sys
input = sys.stdin.readline

def goodmain():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    
    row = list(map(sum,A))
    col = list(map(sum,zip(*A)))
    
    for i in range(H):
        # lambda 引数: 戻り値の式
        # print(" ".join(map(lambda j: str(row[i] + col[j] - A[i][j]), range(W))))

        
        print(*[row[i] + col[j] - A[i][j] for j in range(W)])


def main():
    H,W = map(int,input().split())
    data = []
    row_sums = []
    for _ in range(H):
        lst = list(map(int,input().split()))
        data.append(lst)
        row_sums.append(sum(lst))
    
    col_sums = [sum(x) for x in zip(*data)]
    
    ans = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[i][j] = row_sums[i] + col_sums[j] - data[i][j]
    
    for i in range(H):
        print(*ans[i])

if __name__ == "__main__":
    main()