import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    heap = [(int(x), 0) for x in input_data[2:n+2]]
    
    rem = (n - 1) % (m - 1)
    if rem != 0:
        heap.extend([(0, 0)] * ((m - 1) - rem))
        
    heapq.heapify(heap)
    
    res = 0
    while len(heap) > 1:
        curr_sum = 0
        max_depth = 0
        for _ in range(m):
            w, d = heapq.heappop(heap)
            curr_sum += w
            if d > max_depth:
                max_depth = d
                
        res += curr_sum
        heapq.heappush(heap, (curr_sum, max_depth + 1))
        
    print(res)
    print(heap[0][1])

if __name__ == '__main__':
    main()