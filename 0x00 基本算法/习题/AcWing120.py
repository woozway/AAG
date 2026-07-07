import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    try:
        T = next(iterator)
    except StopIteration:
        return
        
    for _ in range(T):
        n = next(iterator)
        seqs = []
        r = 0
        
        for _ in range(n):
            s = next(iterator)
            e = next(iterator)
            d = next(iterator)
            seqs.append((s, e, d))
            if e > r:
                r = e
                
        def get_sum(x):
            return sum((min(e, x) - s) // d + 1 for s, e, d in seqs if s <= x)
            
        l = 0
        while l < r:
            mid = (l + r) // 2
            if get_sum(mid) % 2 != 0:
                r = mid
            else:
                l = mid + 1
                
        count = get_sum(r) - get_sum(r - 1)
        if count % 2 != 0:
            print(f"{r} {count}")
        else:
            print("There's no weakness.")

if __name__ == '__main__':
    main()