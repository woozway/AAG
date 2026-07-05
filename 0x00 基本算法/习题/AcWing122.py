import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = [0] * (n + 1)
    
    for i in range(1, n + 1):
        s[i] = int(input_data[i]) + s[i - 1]
        
    b = s[n] // n
    c = [0] * n
    
    for i in range(1, n):
        c[i - 1] = i * b - s[i]
    c[n - 1] = 0
    
    c.sort()
    mid = c[n // 2]
    
    res = 0
    for val in c:
        res += abs(val - mid)
        
    print(res)

if __name__ == '__main__':
    main()