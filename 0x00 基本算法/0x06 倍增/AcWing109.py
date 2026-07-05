import sys

def check(l, mid, r, a, b, m, t):
    for i in range(mid + 1, r + 1):
        b[i] = a[i]
    
    b[mid + 1 : r + 1] = sorted(b[mid + 1 : r + 1])
    
    tmp = [0] * (r + 1)
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if j > r or (i <= mid and b[i] <= b[j]):
            tmp[k] = b[i]
            i += 1
        else:
            tmp[k] = b[j]
            j += 1
            
    sum_val = 0
    i, j = l, r
    count = 0
    while i < j and count < m:
        diff = tmp[i] - tmp[j]
        sum_val += diff * diff
        i += 1
        j -= 1
        count += 1
        
    return sum_val <= t, tmp

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    k_cases = int(input_data[idx])
    idx += 1
    
    for _ in range(k_cases):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        t = int(input_data[idx + 2])
        idx += 3
        
        a = [0] * n
        b = [0] * n
        for i in range(n):
            a[i] = int(input_data[idx])
            b[i] = a[i]
            idx += 1
            
        cnt = 0
        l = 0
        while l < n:
            p = 1
            r = l
            while p > 0:
                if r + p < n:
                    is_ok, tmp = check(l, r, r + p, a, b, m, t)
                    if is_ok:
                        r += p
                        for i in range(l, r + 1):
                            b[i] = tmp[i]
                        p <<= 1
                    else:
                        p >>= 1
                else:
                    p >>= 1
            l = r + 1
            cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()