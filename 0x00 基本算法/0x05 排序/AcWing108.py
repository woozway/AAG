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
        
        a1 = []
        for i in range(n * n):
            x = int(input_data[idx])
            idx += 1
            if x != 0:
                a1.append(x)
        
        tmp1 = [0] * len(a1)
        res1 = merge_sort(a1, tmp1, 0, len(a1) - 1)
        
        a2 = []
        for i in range(n * n):
            x = int(input_data[idx])
            idx += 1
            if x != 0:
                a2.append(x)
                
        tmp2 = [0] * len(a2)
        res2 = merge_sort(a2, tmp2, 0, len(a2) - 1)
        
        if (res1 % 2) == (res2 % 2):
            print("TAK")
        else:
            print("NIE")

if __name__ == '__main__':
    main()