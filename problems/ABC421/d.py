import sys

def vec(ch: str):
    if ch == 'U': return (-1, 0)
    if ch == 'D': return (1, 0)
    if ch == 'L': return (0, -1)
    if ch == 'R': return (0, 1)
    raise ValueError

def count_hit(dr, dc, vr, vc, k):
    if vr == 0 and vc == 0:
        return k if (dr == 0 and dc == 0) else 0

    if vr == 0:
        if dr != 0: return 0
        # dc + t*vc = 0
        if vc == 0: return 0
        t = -dc / vc
        return 1 if t.is_integer() and 1 <= t <= k else 0
    if vc == 0:
        if dc != 0: return 0
        if vr == 0: return 0
        t = -dr / vr
        return 1 if t.is_integer() and 1 <= t <= k else 0

    t1 = -dr / vr
    t2 = -dc / vc
    if t1.is_integer() and t1 == t2 and 1 <= t1 <= k:
        return 1
    return 0

def main():
    input = sys.stdin.readline
    rt, ct, ra, ca = map(int, input().split())
    N, M, L = map(int, input().split())

    s = []
    for _ in range(M):
        ch, a = input().split()
        s.append((ch, int(a)))

    t = []
    for _ in range(L):
        ch, b = input().split()
        t.append((ch, int(b)))

    i = j = 0
    rem_s = s[0][1]
    rem_t = t[0][1]
    (sr, sc) = vec(s[0][0])
    (tr, tc) = vec(t[0][0])

    ans = 0
    while i < M and j < L:
        k = min(rem_s, rem_t)

        dr = rt - ra
        dc = ct - ca
        vr = sr - tr
        vc = sc - tc

        ans += count_hit(dr, dc, vr, vc, k)

        rt += sr * k
        ct += sc * k
        ra += tr * k
        ca += tc * k

        rem_s -= k
        rem_t -= k
        if rem_s == 0:
            i += 1
            if i < M:
                sr, sc = vec(s[i][0])
                rem_s = s[i][1]
        if rem_t == 0:
            j += 1
            if j < L:
                tr, tc = vec(t[j][0])
                rem_t = t[j][1]

    print(ans)

if __name__ == "__main__":
    main()
