import sys
import bisect

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    add = [int(x) for x in input_data[1 : n + 1]]
    
    idx = n + 1
    m = int(input_data[idx])
    idx += 1
    
    b = [int(x) for x in input_data[idx : idx + m]]
    idx += m
    c = [int(x) for x in input_data[idx : idx + m]]
    
    all_vals = sorted(list(set(add + b + c)))
    
    def find(x):
        return bisect.bisect_left(all_vals, x)
        
    a = [0] * len(all_vals)
    for x in add:
        a[find(x)] += 1
        
    res = 1
    like = 0
    sub = 0
    
    for i in range(m):
        L = a[find(b[i])]
        l = a[find(c[i])]
        
        if like < L:
            like = L
            sub = l
            res = i + 1
        elif like == L and sub < l:
            sub = l
            res = i + 1
            
    print(res)

if __name__ == '__main__':
    main()