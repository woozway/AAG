import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    cnt = int(input_data[0])
    r = int(input_data[1])
    
    limit = 5001
    r = min(limit, r)
    
    s = [[0] * (limit + 1) for _ in range(limit + 1)]
    
    idx = 2
    for _ in range(cnt):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        idx += 3
        x += 1
        y += 1
        if x <= limit and y <= limit:
            s[x][y] += w
            
    for i in range(1, limit + 1):
        for j in range(1, limit + 1):
            s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
            
    res = 0
    for i in range(r, limit + 1):
        for j in range(r, limit + 1):
            val = s[i][j] - s[i - r][j] - s[i][j - r] + s[i - r][j - r]
            if val > res:
                res = val
                
    print(res)

if __name__ == '__main__':
    main()