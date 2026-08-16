import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    g = [[] for _ in range(n)]
    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        g[u].append((v, w))
        g[v].append((u, w))
        idx += 3
        
    a = [0] * n
    stack = [(0, -1, 0)]
    while stack:
        u, p, s = stack.pop()
        a[u] = s
        for v, w in g[u]:
            if v != p:
                stack.append((v, u, s ^ w))
                
    trie = [[0, 0]]
    for x in a:
        p = 0
        for i in range(30, -1, -1):
            bit = (x >> i) & 1
            if not trie[p][bit]:
                trie.append([0, 0])
                trie[p][bit] = len(trie) - 1
            p = trie[p][bit]
            
    max_xor = 0
    for x in a:
        p = 0
        curr = 0
        for i in range(30, -1, -1):
            bit = (x >> i) & 1
            inv = bit ^ 1
            if trie[p][inv]:
                curr |= (1 << i)
                p = trie[p][inv]
            else:
                p = trie[p][bit]
        if curr > max_xor:
            max_xor = curr
            
    print(max_xor)

if __name__ == '__main__':
    main()