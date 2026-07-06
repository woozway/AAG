import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    cnt = next(iterator)
    R = min(5001, next(iterator))
    
    size = 5002
    s = [[0] * size for _ in range(size)]
    
    for _ in range(cnt):
        x = next(iterator) + 1
        y = next(iterator) + 1
        w = next(iterator)
        s[x][y] += w
        
    for i in range(1, 5002):
        row = s[i]
        prev_row = s[i - 1]
        for j in range(1, 5002):
            row[j] += prev_row[j] + row[j - 1] - prev_row[j - 1]
            
    res = 0
    for i in range(R, 5002):
        row = s[i]
        prev_row = s[i - R]
        for j in range(R, 5002):
            val = row[j] - prev_row[j] - row[j - R] + prev_row[j - R]
            if val > res:
                res = val
                
    print(res)

if __name__ == '__main__':
    main()