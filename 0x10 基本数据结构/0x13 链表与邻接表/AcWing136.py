import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    items = sorted((int(input_data[i]), i) for i in range(1, n + 1))
    a = [(-4000000000, 0)] + items + [(4000000000, 0)]
    
    l = list(range(-1, n + 1))
    r = list(range(1, n + 3))
    
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[a[i][1]] = i
        
    ans = [None] * (n + 1)
    
    for i in range(n, 1, -1):
        j = p[i]
        left, right = l[j], r[j]
        
        left_val = abs(a[left][0] - a[j][0])
        right_val = abs(a[right][0] - a[j][0])
        
        if left_val <= right_val:
            ans[i] = f"{left_val} {a[left][1]}"
        else:
            ans[i] = f"{right_val} {a[right][1]}"
            
        l[right] = left
        r[left] = right
        
    sys.stdout.write("\n".join(ans[2:n+1]) + "\n")

if __name__ == '__main__':
    main()