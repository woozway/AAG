import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    T = int(input_data[idx])
    idx += 1
    
    for _ in range(T):
        m = int(input_data[idx])
        n = int(input_data[idx + 1])
        idx += 2
        
        max_heap = []
        min_heap = []
        
        print(f"{m} {(n + 1) // 2}")
        cnt = 0
        
        for i in range(n):
            t = int(input_data[idx])
            idx += 1
            
            heapq.heappush(max_heap, -t)
            
            if min_heap and min_heap[0] < -max_heap[0]:
                a = heapq.heappop(min_heap)
                b = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, b)
                heapq.heappush(max_heap, -a)
            
            if len(max_heap) > len(min_heap) + 1:
                val = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, val)
                
            if i % 2 == 0:
                print(f"{-max_heap[0]}", end=" ")
                cnt += 1
                if cnt % 10 == 0:
                    print()
        
        if cnt % 10 != 0:
            print()

if __name__ == '__main__':
    main()