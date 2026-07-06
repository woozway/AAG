import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    try:
        n = next(iterator)
        d = next(iterator)
    except StopIteration:
        return
        
    segments = []
    d_sq = d * d
    
    for _ in range(n):
        x = next(iterator)
        y = next(iterator)
        if y > d:
            print("-1")
            return
        
        half_len = math.sqrt(d_sq - y * y)
        segments.append((x + half_len, x - half_len))
        
    segments.sort()
    
    res = 0
    last = -float('inf')
    eps = 1e-6
    
    for right, left in segments:
        if left > last + eps:
            res += 1
            last = right
            
    print(res)

if __name__ == '__main__':
    main()