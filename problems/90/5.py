# DP、ダブリング高速化 
# https://drken1215.hatenablog.com/entry/2021/10/08/231200

import sys
input = sys.stdin.readline  # 高速入力

# ===== 定数定義 =====
MOD = 10**9 + 7   # 答えをこの法で取る
LOG = 62          # N の2進長に十分な上限（~2^61 > 10^18 を想定）

def mul(dpi, dpj, tj):
    """
    dpi:   左側ブロックの「余り分布」(長さ= B)
    dpj:   右側ブロックの「余り分布」(長さ= B)
    tj:    10^{len(右ブロック)} mod B （右を連結する時の10の冪）

    返り値: 左右を連結したときの余り分布
      余り p（左）と 余り q（右）を連結すると new = (p * tj + q) % B
      個数は積: dpi[p] * dpj[q]
    """
    B = len(dpi)                # 余りの総数（=法B）
    res = [0] * B               # 連結後の余り分布を作る箱
    for p in range(B):          # 左の余り
        vp = dpi[p]             # 左で余りpとなる通り数
        if vp == 0:             # 0 通りならスキップで高速化
            continue
        base = (p * tj) % B     # 右ブロックを連結するときの左側拡張分
        for q in range(B):      # 右の余り
            if dpj[q] == 0:     # 0 通りならスキップ
                continue
            res[(base + q) % B] = (res[(base + q) % B] + vp * dpj[q]) % MOD
    return res

def main():
    # ===== 入力 =====
    N, B, K = map(int, input().split())    # N桁 / 法B / 使用可能桁K個
    C = list(map(int, input().split()))    # 使用可能な各桁（0〜9）

    # ===== ten[i] = 10^(2^i) mod B を前計算 =====
    ten = [0] * LOG                 # ten[i] は「長さ2^i のブロック」を連結する時に使う
    ten[0] = 10 % B                 # 10^(1) mod B
    for i in range(1, LOG):         # 二乗して指数を倍々に
        ten[i] = (ten[i - 1] * ten[i - 1]) % B

    # ===== doubling[i] = 長さ 2^i のブロックを1つ並べたときの「余り分布」=====
    doubling = [[0] * B for _ in range(LOG)]

    # 初期化：長さ 1（2^0）ブロックの余り分布（= 1 桁目として置ける桁 C）
    # 1 桁の数 x の B での余りは x % B。各 x ごとに1通りずつある。
    for d in C:
        doubling[0][d % B] = (doubling[0][d % B] + 1) % MOD

    # ダブリング：長さ 2^(i-1) ブロックを2つ連結して長さ 2^i ブロックにする
    # 連結のとき、左側に 10^{2^(i-1)} を掛けるので係数に ten[i-1] を使う
    for i in range(1, LOG):
        doubling[i] = mul(doubling[i - 1], doubling[i - 1], ten[i - 1])

    # ===== N 桁分を 2 進分解で構成 =====
    # res は「現在までに積み上げたブロックの余り分布」。
    # 長さ0（空）では数値は 0 だけなので、余り0が1通り。
    res = [0] * B
    res[0] = 1

    # N の各ビット i を見て、1 なら「長さ 2^i ブロック」を右に連結する
    # 右ブロックの長さは 2^i なので、連結係数は ten[i]（= 10^{2^i} mod B）
    for i in range(LOG):
        if (N >> i) & 1:                   # ビット i が立っているか？
            res = mul(res, doubling[i], ten[i])

    # 余り 0 の通り数が答え
    print(res[0] % MOD)

if __name__ == "__main__":
    main()
