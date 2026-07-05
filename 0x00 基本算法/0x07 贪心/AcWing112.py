import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    d = int(input_data[1])
    
    seg = []
    success = True
    
    idx = 2
    for i in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx += 2
        
        if y > d:
            success = False
            break
        
        len_val = math.sqrt(d * d - y * y)
        seg.append((x + len_val, x - len_val))
    
    if not success:
        print("-1")
    else:
        seg.sort()
        res = 0
        last = -1e10
        
        for r, l in seg:
            if l > last + 1e-6:
                res += 1
                last = r
        print(res)

if __name__ == '__main__':
    main()