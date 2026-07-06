import sys

def sum_geo(p, k, mod):
    if k == 0:
        return 1
    if k % 2 == 0:
        return (1 + (p % mod) * sum_geo(p, k - 1, mod)) % mod
    half = sum_geo(p, k // 2, mod)
    return (1 + pow(p, k // 2 + 1, mod)) * half % mod

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a, b = map(int, input_data)
    if a == 0:
        print(0)
        return
    
    mod = 9901
    res = 1
    d = 2
    temp = a
    while d * d <= temp:
        if temp % d == 0:
            s = 0
            while temp % d == 0:
                s += 1
                temp //= d
            res = res * sum_geo(d, s * b, mod) % mod
        d += 1
    if temp > 1:
        res = res * sum_geo(temp, b, mod) % mod
        
    print(res)

if __name__ == '__main__':
    main()