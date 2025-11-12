import sys

def main():
    s = sys.stdin.readline().strip()
    mid = len(s) // 2
    print(s[:mid] + s[mid+1:])

if __name__ == "__main__":
    main()
