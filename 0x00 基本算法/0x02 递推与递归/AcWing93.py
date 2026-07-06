import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n, m = map(int, input_data[:2])
    
    def dfs(u, cnt, state):
        if cnt + n - u < m:
            return
        if cnt == m:
            print(' '.join(str(i + 1) for i in range(n) if (state >> i) & 1))
            return
            
        dfs(u + 1, cnt + 1, state | (1 << u))
        dfs(u + 1, cnt, state)
        
    dfs(0, 0, 0)

if __name__ == '__main__':
    main()