import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    out = []
    
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        products = [(int(input_data[i + 1]), int(input_data[i])) for i in range(idx, idx + 2 * n, 2)]
        idx += 2 * n
        
        products.sort()
        
        heap = []
        for deadline, profit in products:
            heapq.heappush(heap, profit)
            if len(heap) > deadline:
                heapq.heappop(heap)
                
        out.append(str(sum(heap)))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()