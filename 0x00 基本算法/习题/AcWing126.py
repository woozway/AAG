import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    nums = [int(x) for x in input_data[1:]]
    
    g = [[0] * n for _ in range(n + 1)]
    idx = 0
    for i in range(1, n + 1):
        for j in range(n):
            g[i][j] = g[i - 1][j] + nums[idx]
            idx += 1
            
    res = -float('inf')
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            last = 0
            for k in range(n):
                last = max(last, 0) + g[j][k] - g[i - 1][k]
                if last > res:
                    res = last
                    
    print(res)

if __name__ == '__main__':
    main()