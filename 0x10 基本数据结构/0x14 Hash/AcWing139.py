import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    MASK = 0xFFFFFFFFFFFFFFFF
    P = 131
    
    power = [1]
    out = []
    
    for T, s in enumerate(input_data, 1):
        if s == "END":
            break
            
        n = len(s)
        if len(power) <= n:
            cur = power[-1]
            for _ in range(len(power), n + 1):
                cur = (cur * P) & MASK
                power.append(cur)
                
        b_s = s.encode('ascii')
        
        hl = [0] * (n + 1)
        h = 0
        for i, c in enumerate(b_s):
            h = (h * P + c) & MASK
            hl[i + 1] = h
            
        hr = [0] * (n + 1)
        h = 0
        for i, c in enumerate(reversed(b_s)):
            h = (h * P + c) & MASK
            hr[i + 1] = h
            
        max_len = 0
        for i in range(1, n + 1):
            L = i - max_len - 1
            if L >= 1:
                length = max_len + 2
                hash_l = (hl[i] - hl[L - 1] * power[length]) & MASK
                r_L = n - i + 1
                r_R = n - L + 1
                hash_r = (hr[r_R] - hr[r_L - 1] * power[length]) & MASK
                if hash_l == hash_r:
                    max_len += 2
                    continue
                    
            L = i - max_len
            if L >= 1:
                length = max_len + 1
                hash_l = (hl[i] - hl[L - 1] * power[length]) & MASK
                r_L = n - i + 1
                r_R = n - L + 1
                hash_r = (hr[r_R] - hr[r_L - 1] * power[length]) & MASK
                if hash_l == hash_r:
                    max_len += 1
                    
        out.append(f"Case {T}: {max_len}")
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()