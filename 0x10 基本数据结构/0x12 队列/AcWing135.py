import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + int(input_data[i + 1])
        
    res = -float('inf')
    q = deque([0])
    
    for i in range(1, n + 1):
        if q and q[0] < i - m:
            q.popleft()
            
        res = max(res, s[i] - s[q[0]])
        
        while q and s[q[-1]] >= s[i]:
            q.pop()
            
        q.append(i)
        
    print(res)

if __name__ == '__main__':
    main()