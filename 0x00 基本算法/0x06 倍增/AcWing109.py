N = 500006
n, m, t, w = 0, 0, 0, 0
a, b, c = [0] * N, [0] * N, [0] * N
def merge(l, mid, r):
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if j > r or (i <= mid and b[i] <= b[j]): c[k] = b[i]; i += 1
        else: c[k] = b[j]; j += 1

def f(l, r):
    global n, m, w
    if r > n: r = n
    p = min(m, (r - l + 1) >> 1)
    for i in range(w + 1, r + 1): b[i] = a[i]
    b[w + 1 : r + 1] = sorted(b[w + 1 : r + 1])
    merge(l, w, r)
    num = 0
    for i in range(p): num += (c[r - i] - c[l + i]) ** 2
    return num
    
def Genius_ACM():
    global n, m, t, w, a
    n, m, t = [int(x) for x in input().split()]
    a[1 : n + 1] = [int(x) for x in input().split()]
    ans, l, r = 0, 1, 1
    w = 1
    b[1] = a[1]
    while l <= n:
        p = 1
        while p:
            num = f(l, r + p)
            if num <= t:
                w = r = min(r + p, n)
                for i in range(l, r + 1): b[i] = c[i]
                if r == n: break
                p <<= 1
            else:
                p >>= 1
        ans += 1
        l = r + 1
    print(ans)
    
def main():
    k = int(input())
    for _ in range(k): Genius_ACM()
    
main()