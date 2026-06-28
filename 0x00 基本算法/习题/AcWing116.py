s = [[0] * 4 for _ in range(4)]
a, c = [[False] * 4 for _ in range(4)], [[False]*4 for _ in range(4)]
p = [0]*37
def lowbit(x):
    return x & -x
    
def num(x):
    cnt = 0
    while x:
        cnt += 1
        x -= lowbit(x)
    return cnt
    
def dj(x, y):
    global c
    for i in range(4):
        c[x][i] ^= 1
        c[i][y] ^= 1
    c[x][y] ^= 1

def pd(x):
    global a, c
    c = [row[:] for row in a]
    while x:
        k = lowbit(x) % 37
        dj(p[k] // 4, p[k] % 4)
        x -= lowbit(x)
    for i in range(4):
        for j in range(4):
            if not c[i][j]: return 0
    return 1
    
def main():
    global s, a, p
    for i in range(4): s[i] = input()
    for i in range(4):
        for j in range(4):
            a[i][j] = (s[i][j] == '-')
    ans, x = 17, 0
    for i in range(16): p[(1 << i) % 37] = i
    for i in range(1 << 16):
        n = num(i)
        if n < ans and pd(i):
            ans = n
            x = i
    print(ans)
    while x:
        k = lowbit(x) % 37
        print(p[k] // 4 + 1, p[k] % 4 + 1)
        x -= lowbit(x)

main()