N = 100006
n, d, trie, tot = 0, [0] * N, [[0] * 2 for _ in range(N*33)], 0
head, ver, edge, nxt, v = [0] * N, [0] * (N * 2), [0] * (N * 2), [0] * (N * 2), [0] * N

def dfs(x):
    global n, tot
    i = head[x]
    while i:
        y, z = ver[i], edge[i]
        if v[y]: i = nxt[i]; continue
        v[y] = 1
        d[y] = d[x] ^ z
        dfs(y)
        i = nxt[i]
        
def add(x, y, z):
    global n, tot
    tot += 1; ver[tot] = y; edge[tot] = z
    nxt[tot] = head[x]; head[x] = tot
    
def The_xor_longest_Path():
    global n, tot
    v[0] = 1
    tot = 1
    for _ in range(1, n):
        u, v_, w = [int(x) for x in input().split()]
        add(u, v_, w)
        add(v_, u, w)
        
    dfs(0)
    ans = 0
    for i in range(n):
        p = 1
        for j in range(31, -1, -1):
            k = (d[i] >> j) & 1
            if not trie[p][k]: tot += 1; trie[p][k] = tot
            p = trie[p][k]
        p = 1
        if i:
            w = 0
            for j in range(31, -1, -1):
                k = (d[i] >> j) & 1
                if trie[p][k^1]:
                    w = (w << 1) + (k ^ 1)
                    p = trie[p][k^1]
                else:
                    w = (w << 1) + k
                    p = trie[p][k]
            ans = max(ans, w ^ d[i])
    print(ans)

def main():
    global n, tot
    n = int(input())
    The_xor_longest_Path()
    
main()