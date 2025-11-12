# 辞書順最小 → 貪欲法！

import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    S = input().strip()  # 英小文字のみ
    
    base = ord('a')

    # next_pos[i][c] = 位置 i 以降で文字 c が最初に現れるインデックス（なければ -1）
    # i は 0..N、c は 0..25（'a' を 0 に対応）
    next_pos = [[-1] * 26 for _ in range(N + 1)]

    # 末尾の「i=N 以降」には何もないので -1 のままでOK
    # 後ろから埋めていく：i の行は i+1 行をコピーして、S[i] の文字だけ i に更新
    for i in range(N - 1, -1, -1):
        row = next_pos[i]
        nxt = next_pos[i + 1]
        # まず i+1 の情報をコピー
        # （copy で別オブジェクトにする）
        row[:] = nxt[:]
        # S[i] の文字の列だけ、位置 i で更新
        row[ord(S[i]) - base] = i

    ans = []
    idx = 0  # 次の探索開始位置（左から貪欲に進めていく）
    for taken in range(K):
        # 残り必要な文字数
        rest = K - (taken + 1)

        # 'a' から 'z' を順に試す（辞書順最小を目指す）
        for c in range(26):
            ni = next_pos[idx][c]  # 今の位置 idx 以降での c の最初の出現
            if ni == -1:
                continue  # その文字はもう現れない

            # もしここで ni を採用した場合、右側に残る長さは N - (ni+1)
            # 右側だけで rest 文字が取れれば、採用できる
            if N - (ni + 1) >= rest:
                ans.append(chr(c + base))
                idx = ni + 1  # 次は採用位置の右から探す
                break

    print(''.join(ans))

if __name__ == "__main__":
    main()
