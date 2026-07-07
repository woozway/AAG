import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    try:
        n = next(iterator)
    except StopIteration:
        return
        
    cows = [(next(iterator), next(iterator)) for _ in range(n)]
    
    cows.sort(key=lambda x: x[0] + x[1])
    
    res = -float('inf')
    current_weight = 0
    
    for w, s in cows:
        res = max(res, current_weight - s)
        current_weight += w
        
    print(res)

if __name__ == '__main__':
    main()