import sys

def dfs(g, n):
    if n == 1:
        g[0][0] = 'X'
        return
    
    dfs(g, n - 1)
    
    length = 1
    for i in range(n - 2):
        length *= 3
        
    sx = [0, 1, 2, 2]
    sy = [2, 1, 0, 2]
    
    for k in range(4):
        for i in range(length):
            for j in range(length):
                g[sx[k] * length + i][sy[k] * length + j] = g[i][j]

def main():
    max_len = 1
    for i in range(6):
        max_len *= 3
    
    g = [[' ' for _ in range(max_len)] for _ in range(max_len)]
    dfs(g, 7)
    
    input_data = sys.stdin.read().split()
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == -1:
            break
        
        k = 1
        for i in range(n - 1):
            k *= 3
            
        for i in range(k):
            print("".join(g[i][:k]))
        print('-')

if __name__ == '__main__':
    main()