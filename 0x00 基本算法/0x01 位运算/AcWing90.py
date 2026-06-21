def mul(a, b, p):
    ans = 0
    while b:
        if b & 1: ans = (ans + a) % p
        a = a * 2 % p
        b >>= 1
    return ans
    
def main():
    a = int(input())
    b = int(input())
    p = int(input())
    print(mul(a, b, p))
    
main()