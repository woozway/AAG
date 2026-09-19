import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    a = int(next(it))
    b = int(next(it))
    
    P = 131
    MASK = 0xFFFFFFFFFFFFFFFF
    
    p = [1] * (n * m + 1)
    for i in range(1, n * m + 1):
        p[i] = (p[i - 1] * P) & MASK
        
    hashv = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        row = next(it)
        for j in range(1, m + 1):
            hashv[i][j] = (hashv[i][j - 1] * P + ord(row[j - 1]) - 48) & MASK
            
    S = set()
    p_ab = p[a * b]
    p_b = p[b]
    
    for i in range(b, m + 1):
        s = 0
        l_minus_1 = i - b
        for j in range(1, n + 1):
            val = (hashv[j][i] - hashv[j][l_minus_1] * p_b) & MASK
            s = (s * p_b + val) & MASK
            
            if j > a:
                val_remove = (hashv[j - a][i] - hashv[j - a][l_minus_1] * p_b) & MASK
                s = (s - val_remove * p_ab) & MASK
                
            if j >= a:
                S.add(s)
                
    k = int(next(it))
    out = []
    for _ in range(k):
        s = 0
        for _ in range(a):
            for char in next(it):
                s = (s * P + ord(char) - 48) & MASK
        out.append("1" if s in S else "0")
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()