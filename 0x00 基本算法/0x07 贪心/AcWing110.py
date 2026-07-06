import sys
import bisect
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    n = next(iterator)
    m = next(iterator)
    
    cows = [(next(iterator), next(iterator)) for _ in range(n)]
    
    spf_counts = defaultdict(int)
    for _ in range(m):
        spf_counts[next(iterator)] += next(iterator)
        
    spf_keys = sorted(spf_counts.keys())
    cows.sort(key=lambda x: x[0], reverse=True)
    
    res = 0
    for min_spf, max_spf in cows:
        idx = bisect.bisect_right(spf_keys, max_spf) - 1
        if idx >= 0:
            spf = spf_keys[idx]
            if spf >= min_spf:
                res += 1
                spf_counts[spf] -= 1
                if spf_counts[spf] == 0:
                    spf_keys.pop(idx)
                    
    print(res)

if __name__ == '__main__':
    main()