import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    g = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    idx = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            g[i][j] = int(input_data[idx])
            idx += 1
            g[i][j] += g[i - 1][j]
            
    res = -float('inf')
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            last = 0
            for k in range(1, n + 1):
                col_sum = g[j][k] - g[i - 1][k]
                last = max(last, 0) + col_sum
                res = max(res, last)
                
    print(res)

if __name__ == '__main__':
    main()