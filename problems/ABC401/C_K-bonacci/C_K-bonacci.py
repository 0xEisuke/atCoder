def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = k                            
    a = [1 for i in range(n + 1)]  
    
    for i in range(k, n + 1):    
        a[i] = s                  
        s -= a[i - k]              
        s += a[i]                 
        s %= 10**9               
    
    print(a[n])                    

# def kbonacci(n, k):
#     MOD = 10 ** 9
#     a = [1] * max(n + 1, k)  # 最初のK項は1、それ以降を更新

#     s = sum(a[:k])  # 初期合計値

#     for i in range(k, n + 1):
#         a[i] = s
#         s = (s - a[i - k] + a[i]) % MOD

#     return a[n]

# def main():
#     print(kbonacci(6, 3))   # 期待値: 17
#     print(kbonacci(0, 5))   # 期待値: 1
#     print(kbonacci(5, 1))   # 期待値: 1
#     print(kbonacci(10, 2))  # 期待値: 89（フィボナッチ）
#     print(kbonacci(100000, 1))  # 超でかいけど確認できる（全部1）

if __name__ == "__main__":
    main()
