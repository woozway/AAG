import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    n = next(iterator)
    p = next(iterator)
    h = next(iterator)
    m = next(iterator)
    
    d = [0] * (n + 2)
    d[1] = h
    
    seen = set()
    for _ in range(m):
        a, b = next(iterator), next(iterator)
        if a > b:
            a, b = b, a
            
        if (a, b) not in seen:
            seen.add((a, b))
            d[a + 1] -= 1
            d[b] += 1
            
    for i in range(1, n + 1):
        d[i] += d[i - 1]
        print(d[i])

if __name__ == '__main__':
    main()