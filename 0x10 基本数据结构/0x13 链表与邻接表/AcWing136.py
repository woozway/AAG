from math import inf

N = 100006
a = [[0] * 4 for _ in range(N)] # (a, w, prv, nxt)
b = [0] * N
ans = [[0]*2 for _ in range(N)] # (x, k)

def main():
    n = int(input())
    tmp = [int(x) for x in input().split()]
    for i in range(1, n + 1):
        a[i][:2] = tmp[i - 1], i
    a[1 : n + 1] = sorted(a[1 : n + 1], key=lambda x: (x[0], x[1]))
    for i in range(1, n + 1):
        b[a[i][1]] = i
        a[i][2] = i - 1
        a[i][3] = i + 1
    a[0][0], a[n + 1][0] = -inf, inf
    for i in range(n, 1, -1):
        ans[i][0] = a[a[b[i]][3]][0] - a[b[i]][0]
        ans[i][1] = a[a[b[i]][3]][1]
        if a[b[i]][0] - a[a[b[i]][2]][0] <= ans[i][0]:
            ans[i][0] = a[b[i]][0] - a[a[b[i]][2]][0]
            ans[i][1] = a[a[b[i]][2]][1]
        a[a[b[i]][2]][3] = a[b[i]][3]
        a[a[b[i]][3]][2] = a[b[i]][2]
    for i in range(2, n + 1):
        print(ans[i][0], ans[i][1])
        
main()