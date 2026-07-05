import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    cows = []
    idx = 1
    for i in range(n):
        start = int(input_data[idx])
        end = int(input_data[idx + 1])
        cows.append(((start, end), i))
        idx += 2
        
    cows.sort()
    
    id_arr = [0] * n
    heap = []
    
    for i in range(n):
        start, end = cows[i][0]
        original_idx = cows[i][1]
        
        if not heap or heap[0][0] >= start:
            stall_idx = len(heap)
            id_arr[original_idx] = stall_idx
            heapq.heappush(heap, (end, stall_idx))
        else:
            stall_end, stall_idx = heapq.heappop(heap)
            id_arr[original_idx] = stall_idx
            heapq.heappush(heap, (end, stall_idx))
            
    print(len(heap))
    for i in range(n):
        print(id_arr[i] + 1)

if __name__ == '__main__':
    main()