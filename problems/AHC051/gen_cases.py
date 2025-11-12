# gen_cases.py
# 入力ジェネレータ：問題文の「入力生成方法」に準拠
# - N: 5..20,  M: 10N..50N,  K: N..4N を一様ランダム
# - 入口 (0,5000) を既存点集合Sに入れてから、S内のどの点ともユークリッド距離>100 になるように
#   N+M 個の座標を 0..10000 の整数格子からリジェクトサンプリング
# - 確率 p_{k,j} は rand(1000,9000)×1e-4 → [0.1,0.9] を4桁小数で出力

import argparse
import random
import sys
from math import hypot

LIM = 10_000
MIN_DIST = 100.0  # S内の最小距離（入口含む）

def gen_int(a, b):
    return random.randint(a, b)

def far_enough(x, y, S, min_dist=MIN_DIST):
    for (sx, sy) in S:
        if hypot(x - sx, y - sy) <= min_dist:
            return False
    return True

def sample_points(total_needed, min_dist=MIN_DIST, max_tries=1_000_000):
    """
    入口(0,5000)から始めて、S内のどの点とも距離>min_dist の点を total_needed 個サンプリング。
    """
    S = {(0, 5000)}
    pts = []
    tries = 0
    while len(pts) < total_needed and tries < max_tries:
        tries += 1
        x = gen_int(0, LIM)
        y = gen_int(0, LIM)
        if far_enough(x, y, S, min_dist):
            S.add((x, y))
            pts.append((x, y))
    if len(pts) < total_needed:
        raise RuntimeError(f"Failed to place {total_needed} points with min_dist={min_dist}. "
                           f"Placed={len(pts)}, tries={tries}")
    return pts

def gen_case():
    # N, M, K を範囲から一様ランダム
    N = gen_int(5, 20)
    M = gen_int(10*N, 50*N)
    K = gen_int(N, 4*N)

    # N+M 個の座標をサンプル（前半Nが処理装置、後半Mが分別器サイト）
    pts = sample_points(N + M)
    D = pts[:N]
    S = pts[N:]

    # 確率表 K×N： rand(1000,9000)×1e-4
    P = [[gen_int(1000, 9000) * 1e-4 for _ in range(N)] for _ in range(K)]

    return N, M, K, D, S, P

def print_case(N, M, K, D, S, P, out=sys.stdout):
    print(N, M, K, file=out)
    for x, y in D:
        print(x, y, file=out)
    for x, y in S:
        print(x, y, file=out)
    # 小数は4桁で（1e-4刻みなので情報落ちなし）
    for row in P:
        print(" ".join(f"{v:.4f}" for v in row), file=out)

def main():
    ap = argparse.ArgumentParser(description="Probabilistic Waste Sorting 入力ジェネレータ")
    ap.add_argument("--cases", type=int, default=1, help="生成するケース数")
    ap.add_argument("--seed", type=int, default=None, help="乱数シード")
    ap.add_argument("--prefix", type=str, default="case_", help="保存ファイルのプレフィックス（--stdoutなら無視）")
    ap.add_argument("--stdout", action="store_true", help="標準出力に出す（複数ケースでも連結して出力）")
    ap.add_argument("--min-dist", type=float, default=MIN_DIST, help="点同士の最小距離しきい値")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    for i in range(args.cases):
        N, M, K, D, S, P = gen_case()
        if args.stdout:
            print_case(N, M, K, D, S, P, sys.stdout)
        else:
            path = f"{args.prefix}{i:03d}.txt"
            with open(path, "w") as f:
                print_case(N, M, K, D, S, P, f)
            print(f"wrote {path}")

if __name__ == "__main__":
    main()
