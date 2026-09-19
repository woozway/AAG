import sys

def parse(seq):
    u = 0
    
    def dfs():
        nonlocal u
        u += 1
        children = []
        while u < len(seq) and seq[u] == '0':
            children.append(dfs())
        u += 1
        return '0' + ''.join(sorted(children)) + '1'
        
    return dfs()

def main():
    sys.setrecursionlimit(20000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        a = '0' + input_data[idx] + '1'
        b = '0' + input_data[idx + 1] + '1'
        idx += 2
        
        if parse(a) == parse(b):
            out.append("same")
        else:
            out.append("different")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()