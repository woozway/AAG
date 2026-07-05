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

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    output = []
    for _ in range(t):
        p = int(input_data[idx])
        n = int(input_data[idx + 1])
        idx += 2
        
        res = 0
        for _ in range(n):
            a = int(input_data[idx])
            b = int(input_data[idx + 1])
            idx += 2
            res = (res + qmi(a, b, p)) % p
        output.append(str(res))
        
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    main()