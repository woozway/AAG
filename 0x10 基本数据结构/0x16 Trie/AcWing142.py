import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    trie = [{}]
    cnt = [0]
    
    for _ in range(n):
        p = 0
        for char in next(it):
            if char not in trie[p]:
                trie[p][char] = len(trie)
                trie.append({})
                cnt.append(0)
            p = trie[p][char]
        cnt[p] += 1
        
    out = []
    for _ in range(m):
        p = 0
        res = 0
        for char in next(it):
            if char not in trie[p]:
                break
            p = trie[p][char]
            res += cnt[p]
        out.append(str(res))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()