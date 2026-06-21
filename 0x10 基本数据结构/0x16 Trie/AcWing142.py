N = 1000006
trie, tot, s = [[0] * 27 for _ in range(N)], 1, ""

def add():
    global tot, s
    len_, p = len(s), 1
    for i in range(len_):
        k = ord(s[i]) - ord('a') + 1
        if not trie[p][k]: tot += 1; trie[p][k] = tot
        p = trie[p][k]
    trie[p][0] += 1
    
def get():
    global s
    ans, len_, p = 0, len(s), 1
    for i in range(len_):
        p = trie[p][ord(s[i]) - ord('a') + 1]
        ans += trie[p][0]
    print(ans)
    
def main():
    global s
    n, m = [int(x) for x in input().split()]
    for _ in range(n):
        s = input()
        add()
    for _ in range(m):
        s = input()
        get()

main()