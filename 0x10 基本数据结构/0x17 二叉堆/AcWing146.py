import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = iter(int(x) for x in input_data)
    T = next(it)
    out = []
    
    for _ in range(T):
        m = next(it)
        n = next(it)
        
        a = sorted(next(it) for _ in range(n))
        
        for _ in range(m - 1):
            b = [next(it) for _ in range(n)]
            
            heap = [(b[i] + a[0], 0) for i in range(n)]
            heapq.heapify(heap)
            
            c = []
            for _ in range(n):
                s, p = heapq.heappop(heap)
                c.append(s)
                if p + 1 < n:
                    heapq.heappush(heap, (s - a[p] + a[p + 1], p + 1))
            a = c
            
        out.append(' '.join(map(str, a)))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()