import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    path = []
    
    def dfs(u, state):
        if u == n:
            print(' '.join(map(str, path)))
            return
            
        for i in range(n):
            if not ((state >> i) & 1):
                path.append(i + 1)
                dfs(u + 1, state | (1 << i))
                path.pop()
                
    dfs(0, 0)

if __name__ == '__main__':
    main()