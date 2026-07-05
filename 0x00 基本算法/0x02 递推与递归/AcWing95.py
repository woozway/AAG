import sys
import copy

INF = 0x3f3f3f3f
g = []
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

def turn(x, y):
    for i in range(5):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < 5 and 0 <= b < 5:
            g[a][b] = '1' if g[a][b] == '0' else '0'

def work():
    ans = INF
    for k in range(1 << 5):
        res = 0
        backup = copy.deepcopy(g)
        
        for j in range(5):
            if (k >> j) & 1:
                res += 1
                turn(0, j)
        
        for i in range(4):
            for j in range(5):
                if g[i][j] == '0':
                    res += 1
                    turn(i + 1, j)
        
        is_successful = True
        for j in range(5):
            if g[4][j] == '0':
                is_successful = False
                break
        
        if is_successful:
            ans = min(ans, res)
        
        for i in range(5):
            g[i] = backup[i][:]
            
    if ans > 6:
        return -1
    return ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    curr = 1
    for _ in range(T):
        for i in range(5):
            g.append(list(input_data[curr]))
            curr += 1
        print(work())
        g.clear()

if __name__ == '__main__':
    main()