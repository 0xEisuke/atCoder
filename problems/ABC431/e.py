import sys
from collections import deque

INF = 10**9

# dir: 0=up,1=right,2=down,3=left
DI = [1, 0, -1, 0]
DJ = [0, 1, 0, -1]

def out_dir_for(type_char, in_dir):
    if type_char == 'A':
        return (in_dir + 2) % 4
    if type_char == 'B':
        return in_dir ^ 3
    if type_char == 'C':
        return in_dir ^ 1
    raise ValueError("unknown mirror char")

def solve_case(H, W, S):
    dist = [[[INF]*4 for _ in range(W)] for __ in range(H)]
    dq = deque()

    dist[0][0][3] = 0
    dq.append((0,0,3))

    while dq:
        i,j,in_dir = dq.popleft()
        cur = dist[i][j][in_dir]
        for t in ('A','B','C'):
            out = out_dir_for(t, in_dir)
            ni = i + DI[out]
            nj = j + DJ[out]
            add_cost = 0 if S[i][j] == t else 1
            new_cost = cur + add_cost

            if i == H-1 and j == W-1 and out == 1:
                return new_cost

            if 0 <= ni < H and 0 <= nj < W:
                next_in = (out + 2) % 4
                if new_cost < dist[ni][nj][next_in]:
                    dist[ni][nj][next_in] = new_cost
                    # 0-1 BFS
                    if add_cost == 0:
                        dq.appendleft((ni,nj,next_in))
                    else:
                        dq.append((ni,nj,next_in))
    return -1

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    out_lines = []
    for _ in range(T):
        line = input().split()
        while len(line) == 0:
            line = input().split()
        H = int(line[0]); W = int(line[1])
        S = [list(input().strip()) for __ in range(H)]
        ans = solve_case(H, W, S)
        out_lines.append(str(ans))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
