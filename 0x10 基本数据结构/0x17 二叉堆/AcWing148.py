import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    heap = [int(x) for x in input_data[1:n+1]]
    
    heapq.heapify(heap)
    
    res = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        res += a + b
        heapq.heappush(heap, a + b)
        
    print(res)

if __name__ == '__main__':
    main()