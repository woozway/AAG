N = 730
n, p = 0, [0] * 8
a = [[False] * N for _ in range(N)]

def fractal(k, x, y):
    if k == 1:
        a[x][y] = True
        return
    fractal(k - 1, x, y)
    fractal(k - 1, x, y + 2 * p[k - 1])
    fractal(k - 1, x + p[k - 1], y + p[k - 1]);
    fractal(k - 1, x + 2 * p[k - 1], y);
    fractal(k - 1, x + 2 * p[k - 1], y + 2 * p[k - 1]);
    
def Fractal():
    global n
    fractal(n, 1, 1)
    for i in range(1, p[n] + 1):
        for j in range(1, p[n] + 1):
            print('X' if a[i][j] else ' ', end='')
        print()
    print('-')
    
def main():
    global n
    p[1] = 1
    for i in range(2, 8): p[i] = p[i - 1] * 3
    while True:
        n = int(input())
        if n == -1: break
        Fractal()

main()