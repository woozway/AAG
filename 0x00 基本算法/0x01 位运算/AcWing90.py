import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    a, b, p = map(int, input_data[:3])
    
    res = 0
    while b:
        if b & 1:
            res = (res + a) % p
        a = (a + a) % p
        b >>= 1
        
    print(res)

if __name__ == '__main__':
    main()