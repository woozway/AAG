import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    num_tests = next(iterator)
    
    for _ in range(num_tests):
        m = next(iterator)
        n = next(iterator)
        
        print(f"{m} {(n + 1) // 2}")
        
        max_heap = []
        min_heap = []
        res = []
        
        for i in range(n):
            t = next(iterator)
            heapq.heappush(max_heap, -t)
            
            if min_heap and min_heap[0] < -max_heap[0]:
                a = heapq.heappop(min_heap)
                b = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, b)
                heapq.heappush(max_heap, -a)
                
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                
            if i % 2 == 0:
                res.append(str(-max_heap[0]))
                
        for i in range(0, len(res), 10):
            print(' '.join(res[i:i + 10]))

if __name__ == '__main__':
    main()