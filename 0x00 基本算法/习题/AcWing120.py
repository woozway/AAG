import sys

def get_sum(n, seqs, x):
    res = 0
    for i in range(n):
        s, e, d = seqs[i]
        if s <= x:
            res += (min(e, x) - s) // d + 1
    return res

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    T = int(input_data[idx])
    idx += 1
    
    for _ in range(T):
        n = int(input_data[idx])
        idx += 1
        seqs = []
        l, r = 0, 0
        for i in range(n):
            s = int(input_data[idx])
            e = int(input_data[idx + 1])
            d = int(input_data[idx + 2])
            idx += 3
            seqs.append((s, e, d))
            if e > r:
                r = e
        
        while l < r:
            mid = (l + r) // 2
            if get_sum(n, seqs, mid) % 2 != 0:
                r = mid
            else:
                l = mid + 1
        
        sum_r = get_sum(n, seqs, r)
        sum_r_minus_1 = get_sum(n, seqs, r - 1)
        count = sum_r - sum_r_minus_1
        
        if count % 2 != 0:
            print(f"{r} {count}")
        else:
            print("There's no weakness.")

if __name__ == '__main__':
    main()