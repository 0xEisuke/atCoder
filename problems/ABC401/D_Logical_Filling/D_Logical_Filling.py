#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10**9

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = input().strip()
    
    # まず固定の 'o' の個数を数える
    fixed_o = sum(1 for c in S if c == 'o')
    # 変数部分で追加する必要のある o の個数
    r_required = K - fixed_o
    # r_required は 0以上でなければならない（X が空でない保証より）

    # DP配列の初期化：dp_min[i][state] と dp_max[i][state] (state: 1=置ける, 0=置けない)
    dp_min = [[INF, INF] for _ in range(N+1)]
    dp_max = [[-INF, -INF] for _ in range(N+1)]
    for state in (0,1):
        dp_min[N][state] = 0
        dp_max[N][state] = 0

    # 後ろからDPを計算
    # 状態の意味：状態==1ならこの位置で o を置いてよい（すなわち前が o でない）
    # 状態==0なら前で o を置いたので、この位置は必ず '.' とする
    for i in range(N-1, -1, -1):
        for state in (0,1):
            if state == 0:
                # 強制的に '.' とするので，状態がリセットして1になる
                dp_min[i][0] = dp_min[i+1][1]
                dp_max[i][0] = dp_max[i+1][1]
            else:  # state == 1
                c = S[i]
                if c == 'o':  # 固定されている o
                    # 固定なので，変数 o の加算には含めず、状態は0に遷移
                    dp_min[i][1] = dp_min[i+1][0]
                    dp_max[i][1] = dp_max[i+1][0]
                elif c == '.':  # 固定 '.'
                    dp_min[i][1] = dp_min[i+1][1]
                    dp_max[i][1] = dp_max[i+1][1]
                elif c == '?':
                    # 選択肢2つ： '.' を選ぶ or 'o' を選ぶ（ただし o はこの状態でのみ可能）
                    option_dot_min = dp_min[i+1][1]     # 現在 0 加算
                    option_dot_max = dp_max[i+1][1]
                    option_o_min = 1 + dp_min[i+1][0]     # o を置くなら +1, 次は状態0
                    option_o_max = 1 + dp_max[i+1][0]
                    dp_min[i][1] = min(option_dot_min, option_o_min)
                    dp_max[i][1] = max(option_dot_max, option_o_max)
    
    # 全体として (i=0, state=1) で r_required が実現可能かチェック
    if not (dp_min[0][1] <= r_required <= dp_max[0][1]):
        # この場合は X が空だったはず．
        print(-1)
        return

    # 以下，貪欲に極小解（lex-small）と極大解（lex-large）を構成する。
    # それぞれ，位置 i = 0 から N-1 まで，現在状態 state (初期は1) と残り必要な o (r)
    # に基づいて文字を決定していく。
    
    def construct(mode):
        # mode = "min" なら lex-small，"max" なら lex-large
        res = []
        state = 1   # 初期状態：o を置いてよい
        r = r_required
        for i in range(N):
            c = S[i]
            if state == 0:
                # 前で o を置いたので，この位置は強制的に '.'
                res.append('.')
                state = 1  # '.' の後は o を置ける
                continue
            # state == 1 のとき
            if c in ['o', '.']:
                # 固定文字の場合はそのまま採用．
                res.append(c)
                # 状態更新：もし c=='o'，次は o を置けない (state=0)．
                state = 0 if c == 'o' else 1
            else:  # c == '?'
                # 選択可能．2通りある：
                #  ① 現在 '.' を選んだ場合，次状態は 1, この位置では o は加算されない．
                #  ② 現在 'o' を選ぶ場合，次状態は 0, r を 1 減らす必要がある．
                # 各選択後に，残り区間 (i+1) において
                # 状態 1（または 0）から置ける変数 o の最小／最大値 (dp_min, dp_max) が求まっている。
                #
                # 【極小解の場合】は，できるだけ '.'（小さい方）を選びたい．
                # ただし，もし '.' を選んだ場合に (i+1, state=1) で残り r 個が実現不可能なら，
                # むしろ 'o' を選ぶ必要がある．
                #
                # 【極大解の場合】は逆に，できるだけ 'o' を選びたい．
                #
                # ※ それぞれ，以下の条件で実現可能か確認する：
                #    状態 s で，残り部分で配置できる o の個数の区間が [dp_min[i+1][s], dp_max[i+1][s]]
                #    となっている。これに r または r-1 が入るかをチェックする。
                
                # それぞれの選択肢での実現可能性：
                # 選択 '.' → 次状態は 1, 追加 o = 0, 後半で必要な o は r
                feas_dot = (dp_min[i+1][1] <= r <= dp_max[i+1][1])
                # 選択 'o' → 次状態は 0, 追加 o = 1, 後半で必要な o は r-1
                feas_o = (r > 0 and dp_min[i+1][0] <= r-1 <= dp_max[i+1][0])
                if mode == "min":
                    # できれば '.' を選ぶ
                    if feas_dot:
                        res.append('.')
                        state = 1
                    elif feas_o:
                        res.append('o')
                        state = 0
                        r -= 1
                    else:
                        # ここに来たら本来ありえない
                        res.append('?')
                        state = 1
                else:  # mode == "max"
                    # できれば 'o' を選ぶ
                    if feas_o:
                        res.append('o')
                        state = 0
                        r -= 1
                    elif feas_dot:
                        res.append('.')
                        state = 1
                    else:
                        res.append('?')
                        state = 1
        return "".join(res)
    
    # それぞれ極小解と極大解を構成
    T_small = construct("min")
    T_large = construct("max")
    
    # ここで，両者が同じ位置なら強制文字とし，
    # 異なる箇所は X の中で両方あり得るので '?' とする．
    result = []
    for a, b in zip(T_small, T_large):
        if a == b:
            result.append(a)
        else:
            result.append('?')
    print("".join(result))


if __name__ == '__main__':
    main()
