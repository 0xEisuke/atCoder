import sys

def f(x):
    return sum(int(d) for d in str(x))

def main():
    N = int(sys.stdin.readline())
    A = [1]
    for i in range(1, N + 1):
        A.append(sum(f(A[j]) for j in range(i)))
    print(A[N])

if __name__ == "__main__":
    main()
