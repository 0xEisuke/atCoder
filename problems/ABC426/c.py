import sys

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    next_version = list(range(N + 2))
    pc_count = [0] + [1] * N + [0]

    def find(v: int) -> int:
        root = v
        while next_version[root] != root:
            root = next_version[root]
        while next_version[v] != v:
            nxt = next_version[v]
            next_version[v] = root
            v = nxt
        return root

    out_lines = []
    for _ in range(Q):
        X, Y = map(int, input().split())

        upgraded = 0
        v = find(1)
        while v <= X:
            cnt = pc_count[v]
            if cnt:
                upgraded += cnt
                pc_count[Y] += cnt
                pc_count[v] = 0
            next_version[v] = find(v + 1)
            v = next_version[v]

        out_lines.append(str(upgraded))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
