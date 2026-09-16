import sys

def main():
    sys.setrecursionlimit(2000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n + 1]]

    f = [float('inf')] * (n + 1)
    for i in range(n - 1, -1, -1):
        f[i] = min(f[i + 1], a[i])

    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] < a[j] and f[j + 1] < a[i]:
                g[i].append(j)
                g[j].append(i)

    color = [-1] * n

    def dfs(u, c):
        color[u] = c
        for v in g[u]:
            if color[v] == c:
                return False
            if color[v] == -1 and not dfs(v, 1 - c):
                return False
        return True

    for i in range(n):
        if color[i] == -1 and not dfs(i, 0):
            print(0)
            return

    stk1, stk2 = [], []
    now = 1
    i = 0
    ops = []

    while now <= n:
        if i < n and color[i] == 0 and (not stk1 or stk1[-1] > a[i]):
            stk1.append(a[i])
            ops.append('a')
            i += 1
        elif stk1 and stk1[-1] == now:
            stk1.pop()
            ops.append('b')
            now += 1
        elif i < n and color[i] == 1 and (not stk2 or stk2[-1] > a[i]):
            stk2.append(a[i])
            ops.append('c')
            i += 1
        elif stk2 and stk2[-1] == now:
            stk2.pop()
            ops.append('d')
            now += 1

    print(' '.join(ops))

if __name__ == '__main__':
    main()