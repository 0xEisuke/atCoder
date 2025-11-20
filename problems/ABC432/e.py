import sys
input = sys.stdin.readline

# Fenwick Tree (1-indexed)
def add(bit, idx, delta):
    n = len(bit)
    while idx < n:
        bit[idx] += delta
        idx += idx & -idx

def prefix_sum(bit, idx):
    s = 0
    while idx > 0:
        s += bit[idx]
        idx -= idx & -idx
    return s

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    MAXV = 500000
    size = MAXV + 3

    bit_cnt = [0] * size
    bit_sum = [0] * size

    total_sum = 0
    for v in A:
        add(bit_cnt, v + 1, 1)
        add(bit_sum, v + 1, v)
        total_sum += v

    out_lines = []

    for _ in range(Q):
        t, x, y = map(int, input().split())
        if t == 1:
            idx = x - 1
            old = A[idx]
            if old != y:
                add(bit_cnt, old + 1, -1)
                add(bit_sum, old + 1, -old)
                add(bit_cnt, y + 1, 1)
                add(bit_sum, y + 1, y)
                A[idx] = y
                total_sum += y - old
        else:
            l, r = x, y
            if l > r:
                out_lines.append(str(l * N))
                continue

            if l == 0:
                cnt_l = 0
                sum_l = 0
            else:
                cnt_l = prefix_sum(bit_cnt, l)
                sum_l = prefix_sum(bit_sum, l)

            cnt_r = prefix_sum(bit_cnt, r + 1)
            sum_r = prefix_sum(bit_sum, r + 1)

            ans = l * cnt_l + r * (N - cnt_r) + (sum_r - sum_l)
            out_lines.append(str(ans))

    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
