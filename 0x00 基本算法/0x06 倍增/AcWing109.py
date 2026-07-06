import sys

def get_ints():
    for line in sys.stdin:
        for token in line.split():
            yield int(token)

def main():
    iterator = get_ints()
    
    try:
        k = next(iterator)
    except StopIteration:
        return
        
    for _ in range(k):
        n = next(iterator)
        m = next(iterator)
        t = next(iterator)
        
        a = [next(iterator) for _ in range(n)]
        b = a[:]
        tmp = [0] * n
        
        def check(l, mid, r):
            b[mid + 1:r + 1] = sorted(a[mid + 1:r + 1])
            
            i, j = l, mid + 1
            for idx in range(l, r + 1):
                if j > r or (i <= mid and b[i] <= b[j]):
                    tmp[idx] = b[i]
                    i += 1
                else:
                    tmp[idx] = b[j]
                    j += 1
                    
            total_sum = 0
            i, j = l, r
            pairs = 0
            while i < j and pairs < m:
                diff = tmp[i] - tmp[j]
                total_sum += diff * diff
                if total_sum > t:
                    return False
                i += 1
                j -= 1
                pairs += 1
                
            return True

        cnt = 0
        l = 0
        while l < n:
            p = 1
            r = l
            while p > 0:
                if r + p < n and check(l, r, r + p):
                    r += p
                    b[l:r + 1] = tmp[l:r + 1]
                    p <<= 1
                else:
                    p >>= 1
            l = r + 1
            cnt += 1
            
        print(cnt)

if __name__ == '__main__':
    main()