import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    a = [int(x) for x in input_data[2:n + 2]]
    b = [int(x) for x in input_data[n + 2:n + 2 + m]]
    b.sort()
    
    left = []
    right = []
    
    i = 0
    j = 0
    out = []
    
    while i < n or j < m:
        while j < m and b[j] == i:
            val = heapq.heappop(right)
            out.append(str(val))
            heapq.heappush(left, -val)
            j += 1
            
        if i >= n:
            break
            
        x = a[i]
        if not right or x >= right[0]:
            heapq.heappush(right, x)
        else:
            heapq.heappush(left, -x)
            max_left = -heapq.heappop(left)
            heapq.heappush(right, max_left)
            
        i += 1
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()