from math import inf
N = 200006
a = [[0] * 2 for _ in range(N)]
p = [[] for _ in range(N)]

def main():
    n = int(input())
    for i in range(1, n + 1):
        a[i] = int(input()), i
    a[1 : n + 1] = sorted(a[1 : n + 1])
    t, i = 0, 1
    while i <= n:
        t += 1; p[t].append(a[i][1])
        while a[i][0] == a[i + 1][0]:
            i += 1; p[t].append(a[i][1])
        i += 1
    flag, num, ans = 0, inf, 1
    for i in range(1, t + 1):
        s = len(p[i])
        if flag:
            if num < p[i][0]: num = p[i][s - 1]
            else:
                ans += 1
                flag = 0
                num = p[i][0]
        else:
            if num > p[i][s - 1]: num = p[i][0]
            else:
                flag = 1
                num = p[i][s - 1]
    print(ans)

main()