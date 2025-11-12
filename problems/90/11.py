import sys
input = sys.stdin.readline

def main():
    N = int(input())
    jobs = [tuple(map(int, input().split())) for _ in range(N)]  # (D, C, S)
    
    # 締切の早い順に並べる
    jobs.sort(key=lambda x: x[0])

    maxD = max(d for d, _, _ in jobs)
    dp = [0] * (maxD + 1)  # dp[t]: ちょうど t 日使ったときの最大報酬

    for D, C, S in jobs:
        # この仕事は C〜D 日目の終わりに完了できる
        # 重複選択を避けるため t を降順に回す
        for t in range(D, C - 1, -1):
            dp[t] = max(dp[t], dp[t - C] + S)

    print(max(dp))

if __name__ == "__main__":
    main()
