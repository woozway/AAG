N = 100006
x, y, s = [0] * N, [0] * N, [0] * N
def main():
    n, m, t = [int(k) for k in input().split()]
    for i in range(1, t + 1): x[i], y[i] = [int(k) for k in input().split()]
    row, column = not (t % n), not (t % m)
    if not row and not column:
        print("impossible")
        return
    elif row and column: print("both ", end='')
    elif row: print("row ", end='')
    else: print("column ", end='')
    ans = 0
    if row:
        num = t // n
        a = [0] * N
        for i in range(1, t + 1): a[x[i]] += 1
        for i in range(1, n + 1): a[i] -= num
        s[0] = 0
        for i in range(1, n + 1): s[i] = s[i - 1] + a[i]
        s[1 : n + 1] = sorted(s[1 : n + 1])
        for i in range(1, n // 2 + 1): ans += s[n - i + 1] - s[i]
    if column:
        num = t // m
        a = [0] * N
        for i in range(1, t + 1): a[y[i]] += 1
        for i in range(1, m + 1): a[i] -= num
        s[0] = 0
        for i in range(1, m + 1): s[i] = s[i - 1] + a[i]
        s[1 : m + 1] = sorted(s[1 : m + 1])
        for i in range(1, m // 2 + 1): ans += s[m - i + 1] - s[i]
    print(ans)
    
main()