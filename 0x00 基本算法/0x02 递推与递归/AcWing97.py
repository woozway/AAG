import sys

def qmi(a, b, p):
    a %= p
    res = 1 % p
    while b > 0:
        if b & 1:
            res = (res * a) % p
        a = (a * a) % p
        b >>= 1
    return res

def sum_func(p, k, mod):
    if k == 0:
        return 1
    if k % 2 == 0:
        return (1 + (p % mod) * sum_func(p, k - 1, mod)) % mod
    return (1 + qmi(p, k // 2 + 1, mod)) * sum_func(p, k // 2, mod) % mod

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    B = int(input_data[1])
    mod = 9901
    
    if A == 0:
        print(0)
        return

    res = 1
    d = A
    i = 2
    while i * i <= d:
        if d % i == 0:
            s = 0
            while d % i == 0:
                s += 1
                d //= i
            res = res * sum_func(i, s * B, mod) % mod
        i += 1
    if d > 1:
        res = res * sum_func(d, B, mod) % mod
        
    print(res)

if __name__ == '__main__':
    main()