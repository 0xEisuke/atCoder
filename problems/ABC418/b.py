import sys

def main():
    input = sys.stdin.readline
    s = input().strip()
    n = len(s)
    
    max_rate = 0
    for i in range(n):
        if s[i] == "t":
            for j in range(i + 2, n):
                if s[j] == "t":
                    count = 0
                    for k in range(i + 1, j):
                        if s[k] == "t":
                            count += 1
                    rate = count / (j - i - 1)
                    max_rate = max(max_rate, rate)

    print(max_rate)

if __name__ == "__main__":
    main()