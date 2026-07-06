import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    def dfs(u, state):
        if u == n:
            print(' '.join(str(i + 1) for i in range(n) if (state >> i) & 1))
            return
            
        dfs(u + 1, state)
        dfs(u + 1, state | (1 << u))
        
    dfs(0, 0)

if __name__ == '__main__':
    main()