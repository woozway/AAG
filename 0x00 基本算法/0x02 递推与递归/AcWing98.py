import sys
import math

def calc(n, m):
    if n == 0:
        return 0, 0
    
    length = 1 << (n - 1)
    cnt = 1 << (2 * n - 2)
    x, y = calc(n - 1, m % cnt)
    z = m // cnt
    
    if z == 0:
        return y, x
    elif z == 1:
        return x, y + length
    elif z == 2:
        return x + length, y + length
    else:
        return 2 * length - 1 - y, length - 1 - x

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    t = next(iterator)
    
    for _ in range(t):
        n = next(iterator)
        a = next(iterator)
        b = next(iterator)
        
        ax, ay = calc(n, a - 1)
        bx, by = calc(n, b - 1)
        
        dist = math.hypot(ax - bx, ay - by) * 10
        print(round(dist))

if __name__ == '__main__':
    main()