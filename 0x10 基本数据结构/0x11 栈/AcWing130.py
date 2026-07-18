import sys

def get_pow(n, p):
    s = 0
    while n:
        n //= p
        s += n
    return s

def main():
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(1000000)
        
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    limit = 2 * n
    
    st = [False] * (limit + 1)
    primes = []
    
    for i in range(2, limit + 1):
        if not st[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                st[j] = True
                
    q = [0] * (limit + 1)
    for p in primes:
        q[p] = get_pow(limit, p) - get_pow(n, p) * 2
        
    k = n + 1
    for p in primes:
        if p > k:
            break
        while k % p == 0:
            k //= p
            q[p] -= 1
            
    res = 1
    for p in primes:
        if q[p] > 0:
            res *= pow(p, q[p])
            
    print(res)

if __name__ == '__main__':
    main()