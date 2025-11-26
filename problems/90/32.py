# bit DP
# この手の「n 人いて、各人を 1 回ずつ使って順列を作る + 何か条件」は典型的にこういう DP にする

# mask: 今までに使った選手の集合（bitmask）
# j: 最後に使った選手
# dp[mask][j] = その状態までの最小時間

import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    
    # data[j][i] = 選手 j が i 区間目を走ったときの時間
    data = [list(map(int, input().split())) for _ in range(n)]
    
    m = int(input())
    bad_pairs = [set() for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        bad_pairs[x].add(y)
        bad_pairs[y].add(x)
    
    INF = 10**18
    # dp[mask][j] = mask に含まれる選手が走ってきて、
    #               最後に使った選手が j のときの最小時間
    # mask は「すでに使った選手の集合」を表すビット集合（0〜2^n-1）
    dp = [[INF] * n for _ in range(1 << n)]
    
    # 最初の区間（0 区間目）として j を選ぶ
    for j in range(n):
        mask = 1 << j
        dp[mask][j] = data[j][0]
    
    # 全ての mask について遷移
    for mask in range(1 << n):
        # すでに選んだ人数 = 今いる区間数
        # これが i とすると、次に埋めるのは i 区間目（0-index）
        i = mask.bit_count()
        if i == 0 or i >= n:
            # i == 0 はまだ誰も選んでない（初期状態）なのでスキップ
            # i >= n はもう全員使っているのでスキップ
            continue
        
        for last in range(n):
            if not (mask & (1 << last)):
                continue  # last が mask に含まれていない
            cur = dp[mask][last]
            if cur == INF:
                continue
            
            # 次に選ぶ選手 next（i 区間目を担当）
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue  # すでに使った選手は使えない（各選手1回）
                # 直前の選手 last と nxt の組が悪いペアならダメ
                if nxt in bad_pairs[last]:
                    continue
                nmask = mask | (1 << nxt)
                # i 区間目を nxt が走る
                cost = cur + data[nxt][i]
                if cost < dp[nmask][nxt]:
                    dp[nmask][nxt] = cost
    
    full = (1 << n) - 1  # 全員使った状態
    ans = min(dp[full])
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    main()
