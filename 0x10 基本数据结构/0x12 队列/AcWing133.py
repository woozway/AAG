import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n, m, q, u, v, t = map(int, input_data[:6])
    
    q1 = deque(sorted((int(x) for x in input_data[6:6+n]), reverse=True))
    q2 = deque()
    q3 = deque()
    
    def get_max():
        v1 = q1[0] if q1 else -float('inf')
        v2 = q2[0] if q2 else -float('inf')
        v3 = q3[0] if q3 else -float('inf')
        
        if v1 >= v2 and v1 >= v3:
            return q1.popleft()
        if v2 >= v1 and v2 >= v3:
            return q2.popleft()
        return q3.popleft()

    delta = 0
    ans1 = []
    for i in range(1, m + 1):
        x = get_max() + delta
        if i % t == 0:
            ans1.append(str(x))
        
        left = x * u // v
        right = x - left
        
        delta += q
        q2.append(left - delta)
        q3.append(right - delta)
        
    ans2 = []
    for i in range(1, n + m + 1):
        x = get_max() + delta
        if i % t == 0:
            ans2.append(str(x))
            
    sys.stdout.write(" ".join(ans1) + "\n")
    sys.stdout.write(" ".join(ans2) + "\n")

if __name__ == '__main__':
    main()