N = 100006
p = [[0] * 4 for _ in range(N)] # d, prv, nxt, th
h = [[0] * 2 for _ in range(N)] # D, tp
tot = 0

def up(i):
    while i > 1:
        if h[i][0] < h[i >> 1][0]:
            h[i], h[i >> 1] = h[i >> 1], h[i]
            p[h[i][1]][3], p[h[i >> 1][1]][3] = p[h[i >> 1][1]][3], p[h[i][1]][3]
            i >>= 1
        else: return

def down(i):
    global tot
    ii = i << 1
    while ii <= tot:
        if ii < tot and h[ii][0] > h[ii + 1][0]: ii += 1
        if h[ii][0] < h[i][0]:
            h[ii], h[i] = h[i], h[ii]
            p[h[ii][1]][3], p[h[i][1]][3] = p[h[i][1]][3], p[h[ii][1]][3]
            i = ii; ii = i << 1
        else: return
    
def DeL(i):
    p[p[i][1]][2] = p[i][2]
    p[p[i][2]][1] = p[i][1]
    
def DeH(i):
    global tot
    h[i], h[tot] = h[tot], h[i]
    p[h[i][1]][3], p[h[tot][1]][3] = p[h[tot][1]][3], p[h[i][1]][3]
    tot -= 1
    up(i), down(i)
    
def main():
    global tot
    n, k = [int(x) for x in input().split()]
    pre = int(input())
    for i in range(1, n):
        w = int(input())
        tot += 1; p[i] = [w - pre, i - 1, i + 1, tot]
        pre = w
        h[tot] = [p[i][0], i]
        up(tot)
    ans = 0
    for _ in range(k):
        ans += h[1][0]
        tp0 = h[1][1]
        if not p[tp0][1] or p[tp0][2] == n:
            if not p[tp0][1]:
                DeH(p[p[tp0][2]][3])
                DeL(p[tp0][2])
            else:
                DeH(p[p[tp0][1]][3])
                DeL(p[tp0][1])
            DeL(tp0)
            DeH(1)
        else:
            h[1][0] = p[p[tp0][1]][0] + p[p[tp0][2]][0] - p[tp0][0]
            p[tp0][0] = h[1][0]
            down(1)
            DeH(p[p[tp0][1]][3])
            DeH(p[p[tp0][2]][3])
            DeL(p[tp0][1])
            DeL(p[tp0][2])
    print(ans)
    
main()