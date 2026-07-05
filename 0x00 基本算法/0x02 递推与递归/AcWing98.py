import sys
import math

def calc(n, m):
    if n == 0:
        return (0, 0)
    
    len_val = 1 << (n - 1)
    cnt = 1 << (2 * (n - 1))
    
    pos = calc(n - 1, m % cnt)
    x, y = pos[0], pos[1]
    z = m // cnt
    
    if z == 0:
        return (y, x)
    elif z == 1:
        return (x, y + len_val)
    elif z == 2:
        return (x + len_val, y + len_val)
    else:
        return (-y + 2 * len_val - 1, -x + len_val - 1)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        a = int(input_data[idx + 1])
        b = int(input_data[idx + 2])
        idx += 3
        
        ac = calc(n, a - 1)
        bc = calc(n, b - 1)
        
        dx = ac[0] - bc[0]
        dy = ac[1] - bc[1]
        
        dist = math.sqrt(dx * dx + dy * dy) * 10
        results.append(str(int(round(dist))))
        
    print('\n'.join(results))

if __name__ == '__main__':
    main()