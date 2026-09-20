import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    q = int(input_data[2])
    
    a = ' ' + input_data[3]
    b = ' ' + input_data[4] + '#'
    
    ne = [0] * (m + 2)
    f = [0] * (m + 2)
    
    j = 0
    for i in range(2, m + 1):
        while j > 0 and b[j + 1] != b[i]:
            j = ne[j]
        if b[j + 1] == b[i]:
            j += 1
        ne[i] = j
        
    j = 0
    for i in range(1, n + 1):
        while j > 0 and b[j + 1] != a[i]:
            j = ne[j]
        if b[j + 1] == a[i]:
            j += 1
        f[j] += 1
        
    for i in range(m, 0, -1):
        f[ne[i]] += f[i]
        
    out = []
    for k in range(5, 5 + q):
        x = int(input_data[k])
        out.append(str(f[x] - f[x + 1]))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()