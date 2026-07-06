import sys
import math

def calc(n, m):
    if n == 0:
        return 0, 0
    
    len_side = 1 << (n - 1)
    cnt = 1 << (2 * (n - 1))
    x, y = calc(n - 1, m % cnt)
    z = m // cnt
    
    if z == 0:
        return y, x
    if z == 1:
        return x, y + len_side
    if z == 2:
        return x + len_side, y + len_side
    return 2 * len_side - 1 - y, len_side - 1 - x

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n, a, b = map(int, input_data[idx:idx + 3])
        idx += 3
        
        ax, ay = calc(n, a - 1)
        bx, by = calc(n, b - 1)
        
        dist = math.sqrt((ax - bx)**2 + (ay - by)**2) * 10
        print(f"{round(dist)}")

if __name__ == '__main__':
    main()