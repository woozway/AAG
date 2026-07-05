import sys
import bisect

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    cows = []
    idx = 2
    for i in range(n):
        cows.append((int(input_data[idx]), int(input_data[idx + 1])))
        idx += 2
        
    spf_map = {}
    for i in range(m):
        s = int(input_data[idx])
        c = int(input_data[idx + 1])
        spf_map[s] = spf_map.get(s, 0) + c
        idx += 2
        
    cows.sort()
    
    spf_keys = sorted(spf_map.keys())
    
    res = 0
    for i in range(n - 1, -1, -1):
        min_spf, max_spf = cows[i]
        
        pos = bisect.bisect_right(spf_keys, max_spf)
        if pos > 0:
            spf_val = spf_keys[pos - 1]
            if spf_val >= min_spf:
                res += 1
                spf_map[spf_val] -= 1
                if spf_map[spf_val] == 0:
                    spf_keys.pop(pos - 1)
                    del spf_map[spf_val]
                    
    print(res)

if __name__ == '__main__':
    main()