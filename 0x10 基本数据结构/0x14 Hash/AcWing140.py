from functools import cmp_to_key
N, M = 300010, 10 ** 9 + 7
f, p, sa, height = [0] * N, [0] * N, [0] * N, [0] * N
n, s = 0, ['0'] * N

def H(l, r):
    return (f[r] - f[l - 1] * p[r - l + 1]) % M

def lcp(x, y):
    global n
    l, r = 0, min(n - x + 1, n - y + 1)
    while l < r:
        mid = (l + r + 1) >> 1
        if H(x, x + mid - 1) == H(y, y + mid - 1): l = mid
        else: r = mid - 1
    return l

def cmpr(x, y):
    l = lcp(x, y)
    if s[x + l] < s[y + l]: return -1
    elif s[x + l] > s[y + l]: return 1
    else: return 0

def calc_height():
    global n
    for i in range(2, n + 1): height[i] = lcp(sa[i - 1], sa[i])

# TLE
def main():
    global n
    t = input(); n = len(t)
    s[1 : n + 1] = list(t)
    p[0] = 1
    for i in range(1, n + 1):
        sa[i] = i
        f[i] = (f[i - 1] * 131 + ord(s[i])) % M
        p[i] = (p[i - 1] * 131) % M
    sa[1 : n + 1] = sorted(sa[1 : n + 1], key=cmp_to_key(cmpr))
    calc_height()
    for i in range(1, n + 1): print("%d " %(sa[i] - 1), end='')
    print()
    for i in range(1, n + 1): print("%d " %height[i], end='')
    print()

main()