import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    p = int(input_data[1])
    h = int(input_data[2])
    m = int(input_data[3])
    
    d = [0] * (n + 2)
    d[1] = h
    
    existed = set()
    idx = 4
    for _ in range(m):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        
        if a > b:
            a, b = b, a
        
        if (a, b) not in existed:
            existed.add((a, b))
            d[a + 1] -= 1
            d[b] += 1
            
    current_height = 0
    for i in range(1, n + 1):
        current_height += d[i]
        print(current_height)

if __name__ == '__main__':
    main()