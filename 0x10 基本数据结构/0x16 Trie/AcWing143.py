N = 100006 * 33
trie = [[0] * 2 for _ in range(N)]

def main():
    n = int(input())
    ans, t = 0, 1
    aa = [int(x) for x in input().split()]
    for i in range(1, n + 1):
        a, p = aa[i - 1], 1
        for j in range(31, -1, -1):
            k = (a >> j) & 1
            if not trie[p][k]: t += 1; trie[p][k] = t
            p = trie[p][k]
        p = 1
        if i > 1:
            w = 0
            for j in range(31, -1, -1):
                k = (a >> j) & 1
                if trie[p][k ^ 1]:
                    w = (w << 1) + (k ^ 1)
                    p = trie[p][k ^ 1]
                else:
                    w = (w << 1) + k
                    p = trie[p][k]
            ans = max(ans, w ^ a)
    print(ans)

main()