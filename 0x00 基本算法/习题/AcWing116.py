import sys

def main():
    N = 4
    change = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                change[i][j] += (1 << (i * N + k)) + (1 << (k * N + j))
            change[i][j] -= (1 << (i * N + j))

    state = 0
    lines = sys.stdin.read().split()
    for i in range(N):
        for j in range(N):
            if lines[i][j] == '+':
                state += (1 << (i * N + j))

    path = []
    
    for i in range(1 << 16):
        now = state
        temp = []
        for j in range(16):
            if (i >> j) & 1:
                x = j // 4
                y = j % 4
                now ^= change[x][y]
                temp.append((x, y))
        
        if now == 0:
            if not path or len(path) > len(temp):
                path = temp

    print(len(path))
    for p in path:
        print(f"{p[0] + 1} {p[1] + 1}")

if __name__ == '__main__':
    main()