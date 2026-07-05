import sys

def merge_sort(a, tmp, l, r):
    if l >= r:
        return 0
    
    mid = (l + r) // 2
    res = merge_sort(a, tmp, l, mid) + merge_sort(a, tmp, mid + 1, r)
    
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if j > r or (i <= mid and a[i] <= a[j]):
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
            res += (mid - i + 1)
            
    for k in range(l, r + 1):
        a[k] = tmp[k]
        
    return res

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            break
            
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = int(input_data[idx])
            idx += 1
            
        tmp = [0] * (n + 1)
        print(merge_sort(a, tmp, 1, n))

if __name__ == '__main__':
    main()