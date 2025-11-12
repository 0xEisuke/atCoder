# デバッグ用の簡単なテストケース作成
# 冒険者が確認したマスにトレントを配置してしまう問題を再現

def create_test_case():
    # 5x5のグリッドで簡単なテストケース
    test_input = """5 4 4
.....
.....
.....
.....
....F
0 2
1
2 2
1 3
1
3 3
"""
    with open("test_input.txt", "w") as f:
        f.write(test_input)
    print("テストケースを作成しました: test_input.txt")

if __name__ == "__main__":
    create_test_case()