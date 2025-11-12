import sys
from collections import Counter

def main():
    input = sys.stdin.readline
    s = input().strip()
    counter = Counter(s)
    for ch,v in counter.items():
        if v == 1:
            print(ch)

if __name__ == "__main__":
    main()