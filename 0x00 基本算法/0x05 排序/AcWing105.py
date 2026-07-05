import sys

def calc(n, a):
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]
        
    if s[n] % n != 0:
        return -1
        
    b = s[n] // n
    c = [0] * n
    for i in range(1, n):
        c[i] = i * b - s[i]
        
    c.sort()
    
    mid = c[n // 2]
    res = 0
    for x in c:
        res += abs(x - mid)
    return res

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    row = [0] * (n + 1)
    col = [0] * (m + 1)
    
    idx = 3
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx += 2
        row[x] += 1
        col[y] += 1
        
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