import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    k = int(input_data[1])
    
    points = [int(x) for x in input_data[2:n+2]]
    d = [0] * (n + 3)
    
    for i in range(1, n):
        d[i + 1] = points[i] - points[i - 1]
        
    d[1] = d[n + 1] = 10**15
    
    l = list(range(-1, n + 2))
    r = list(range(1, n + 4))
    
    deleted = [False] * (n + 3)
    
    heap = [(d[i], i) for i in range(1, n + 2)]
    heapq.heapify(heap)
    
    res = 0
    for _ in range(k):
        while heap:
            v, p = heapq.heappop(heap)
            if not deleted[p] and v == d[p]:
                break
                
        left = l[p]
        right = r[p]
        
        deleted[left] = True
        deleted[right] = True
        
        r[l[left]] = r[left]
        l[r[left]] = l[left]
        
        r[l[right]] = r[right]
        l[r[right]] = l[right]
        
        res += v
        
        d[p] = d[left] + d[right] - d[p]
        heapq.heappush(heap, (d[p], p))
        
    print(res)

if __name__ == '__main__':
    main()