# stdin_templates.py
# 標準入力の受け取り方まとめ（Python3）

import sys
input = sys.stdin.readline

# 1. 1つの整数
# 例: 1
n = int(input())
print(f"n = {n}")

# 2. 複数の整数（1行）
# 例: 1 3 5 2
arr = list(map(int, input().split()))
print(f"arr = {arr}")

# 3. 文字列（空白なし）
# 例: stringtext
s = input().strip()
print(f"s = '{s}'")

# 4. 複数行まとめて読み込み
# 例: 複数行の入力をリストに格納
lines = sys.stdin.read().splitlines()
line_a = lines[0].strip()  # 1行目
line_b = lines[1].strip()  # 2行目
line_c_to_d = lines[2:6]  # 3行目から6行目まで
line_e = lines[6:].strip()  # 7行目以降
print(f"line_a = '{line_a}'")
print(f"line_b = '{line_b}'")
print(f"line_c_to_d = {line_c_to_d}")
print(f"line_e = '{line_e}'")

# 5. n行のリスト
n = int(input())
lines = [input().strip() for _ in range(n)]
print(f"lines = {lines}")
