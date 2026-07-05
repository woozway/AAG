import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    w = []
    idx = 1
    for i in range(n):
        w.append([int(x) for x in input_data[idx : idx + n]])
        idx += n
        
    f = [[0x3f3f3f3f] * n for _ in range(1 << n)]
    f[1 << 0][0] = 0
    
    for i in range(1 << n):
        for j in range(n):
            if (i >> j) & 1:
                for k in range(n):
                    if (i >> k) & 1:
                        f[i][j] = min(f[i][j], f[i ^ (1 << j)][k] + w[k][j])
                            
    print(f[(1 << n) - 1][n - 1])

if __name__ == '__main__':
    main()