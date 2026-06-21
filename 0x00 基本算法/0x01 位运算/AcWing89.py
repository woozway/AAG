def power(a, b, p):
    ans = 1 % p
    while b:
        if b & 1: ans = ans * a % p
        a = a * a % p
        b >>= 1
    return ans

def main():
    s = input()
    a, b, p = [int(x) for x in s.split()]
    print(power(a, b, p))
    
main()