import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = iter(input_data)
    s = next(it)
    n = len(s)
    
    h = [0] * (n + 1)
    power = [1] * (n + 1)
    
    P = 131
    MOD = 1 << 64
    
    for i, char in enumerate(s, 1):
        h[i] = (h[i - 1] * P + ord(char) - 96) % MOD
        power[i] = (power[i - 1] * P) % MOD
        
    m = int(next(it))
    
    def get_hash(l, r):
        return (h[r] - h[l - 1] * power[r - l + 1]) % MOD
        
    results = [
        "Yes" if get_hash(int(l1), int(r1)) == get_hash(int(l2), int(r2)) else "No"
        for l1, r1, l2, r2 in zip(it, it, it, it)
    ]
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    main()