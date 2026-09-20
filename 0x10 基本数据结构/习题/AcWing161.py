import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = iter(input_data)
    T = int(next(it))
    out = []
    
    for _ in range(T):
        n = int(next(it))
        trie = {}
        valid = True
        
        for _ in range(n):
            s = next(it)
            if not valid:
                continue
                
            node = trie
            has_new = False
            has_found = False
            
            for char in s:
                if char not in node:
                    node[char] = {}
                    has_new = True
                node = node[char]
                if '#' in node:
                    has_found = True
                    
            node['#'] = True
            
            if not has_new or has_found:
                valid = False
                
        out.append("YES" if valid else "NO")
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()