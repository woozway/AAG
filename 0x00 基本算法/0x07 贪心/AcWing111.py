import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    n = next(iterator)
    
    cows = []
    for i in range(n):
        start = next(iterator)
        end = next(iterator)
        cows.append(((start, end), i))
        
    cows.sort()
    
    heap = []
    stall_ids = [0] * n
    
    for (start, end), original_idx in cows:
        if heap and heap[0][0] < start:
            _, stall_num = heapq.heappop(heap)
            stall_ids[original_idx] = stall_num
            heapq.heappush(heap, (end, stall_num))
        else:
            stall_num = len(heap) + 1
            stall_ids[original_idx] = stall_num
            heapq.heappush(heap, (end, stall_num))
            
    print(len(heap))
    for i in range(n):
        print(stall_ids[i])

if __name__ == '__main__':
    main()