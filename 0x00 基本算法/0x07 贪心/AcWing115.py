N = 1006
n, r = 0, 0
fa, nxt, lst, num = [0] * N, [0] * N, [0] * N, [0] * N
c, d, tot, v = [0] * N, [0] * N, [0] * N, [0] * N
def Color_a_Tree():
    global n, r, fa, nxt, lst, num, c, d, tot, v
    c[1 : n + 1] = [int(x) for x in input().split()]
    nxt[1 : n + 1] = list(range(1, n + 1))
    lst[1 : n + 1] = list(range(1, n + 1))
    num[1 : n + 1] = [1] * n
    tot[1 : n + 1] = c[1 : n + 1][:]
    d = c[:]
    for _ in range(1, n):
        a, b = map(int, input().split())
        fa[b] = a
    for i in range(1, n):
        p, k = 0, 0
        for j in range(1, n + 1):
            if j != r and not v[j] and c[j] > k:
                k = c[j]
                p = j
        f = fa[p]
        while v[f]: fa[p] = f = fa[f]
        nxt[lst[f]] = p
        lst[f] = lst[p]
        num[f] += num[p]
        tot[f] += tot[p]
        c[f] = tot[f] / num[f]
        v[p] = 1
    ans = 0
    for i in range(1, n + 1):
        ans += i * d[r]
        r = nxt[r]
    print(ans)

def main():
    global n, r
    n, r = map(int, input().split())
    Color_a_Tree()

main()