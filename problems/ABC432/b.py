import sys
input = sys.stdin.readline

def main():
    x = int(input())
    digits = list(str(x))
    digits.sort()
    if digits[0] == '0':
        for i in range(1, len(digits)):
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break
    print(int(''.join(digits)))

if __name__ == "__main__":
    main()