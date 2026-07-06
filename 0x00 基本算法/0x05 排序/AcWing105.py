import sys

def calc(size, arr):
    total = sum(arr)
    if total % size != 0:
        return -1
        
    target = total // size
    c = [0] * size
    curr = 0
    for i in range(size - 1):
        curr += arr[i]
        c[i] = (i + 1) * target - curr
        
    c.sort()
    median = c[size // 2]
    return sum(abs(x - median) for x in c)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    n = next(iterator)
    m = next(iterator)
    t = next(iterator)
    
    row = [0] * n
    col = [0] * m
    
    for _ in range(t):
        row[next(iterator) - 1] += 1
        col[next(iterator) - 1] += 1
        
    res1 = calc(n, row)
    res2 = calc(m, col)
    
    if res1 != -1 and res2 != -1:
        print(f"both {res1 + res2}")
    elif res1 != -1:
        print(f"row {res1}")
    elif res2 != -1:
        print(f"column {res2}")
    else:
        print("impossible")

if __name__ == '__main__':
    main()