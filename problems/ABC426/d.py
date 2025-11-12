import sys

def forced_peel_cost(s: str, bad: str) -> int:
    n = len(s)
    pos = [i for i, ch in enumerate(s) if ch == bad]
    m = len(pos)
    if m == 0:
        return 0

    left_gaps = [pos[0]]
    for k in range(1, m):
        left_gaps.append(pos[k] - pos[k - 1] - 1)

    right_gaps = [n - 1 - pos[-1]]
    for k in range(m - 1, 0, -1):
        right_gaps.append(pos[k] - pos[k - 1] - 1)

    il = ir = 0
    zL = left_gaps[0]
    zR = right_gaps[0]
    forced = 0
    remaining = m

    while remaining > 0:
        if zL > 0 and zR > 0:
            if zL <= zR:
                forced += zL
                zL = 0
            else:
                forced += zR
                zR = 0
            continue

        if zL == 0:
            remaining -= 1
            il += 1
            zL = left_gaps[il] if il < len(left_gaps) else 0
            continue

        if zR == 0:
            remaining -= 1
            ir += 1
            zR = right_gaps[ir] if ir < len(right_gaps) else 0
            continue

    return m + 2 * forced


def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    out = []
    for _ in range(T):
        N = int(input().strip())
        S = input().strip()
        ans0 = forced_peel_cost(S, '1')
        ans1 = forced_peel_cost(S, '0')
        out.append(str(min(ans0, ans1)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
