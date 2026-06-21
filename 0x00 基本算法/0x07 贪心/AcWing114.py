N = 1006
n, p = 0, [[0] * 2 for _ in range(N)]
k, lk, ans, la, ans0, la0 = [0] * 4 * N, 1, [0] * 4 * N, 1, [0] * 4 * N, 1
def gj1(x):
    global k, lk
    for i in range(1, lk + 1): k[i] *= x
    lk += 4
    for i in range(1, lk + 1):
        k[i + 1] += k[i] // 10
        k[i] %= 10
    while not k[lk]: lk -= 1

def gj2(x):
    global k, lk, ans0, la0
    w, flag = 0, True
    for i in range(lk, 0, -1):
        w = w * 10 + k[i]
        ans0[i] = w // x
        w %= x
        if ans0[i] and flag:
            la0 = i
            flag = False

def pd():
    global ans, la, ans0, la0
    if la != la0: return la < la0
    for i in range(la, 0, -1):
        if ans[i] != ans0[i]: return ans[i] < ans0[i]
    return 0
    
def main():
    global n, p, k, ans, ans0, la, la0
    n = int(input())
    for i in range(n+1): p[i] = [int(x) for x in input().split()]
    p[1 : n + 1] = sorted(p[1 : n + 1], key=lambda x: x[0] * x[1])
    k[1] = 1
    gj1(p[0][0])
    for i in range(1, n + 1):
        gj2(p[i][1])
        if pd():
            ans = ans0[:]
            la = la0
        gj1(p[i][0])
    for i in range(la, 0, -1): print(ans[i], end='')
    
main()