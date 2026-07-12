import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    remain = 20
    path = []
    stk = []
    
    def dfs(u):
        nonlocal remain
        if not remain:
            return
            
        if len(path) == n:
            remain -= 1
            print("".join(map(str, path)))
            return
            
        if stk:
            val = stk.pop()
            path.append(val)
            dfs(u)
            stk.append(path.pop())
            
        if u <= n:
            stk.append(u)
            dfs(u + 1)
            stk.pop()
            
    dfs(1)

if __name__ == '__main__':
    main()