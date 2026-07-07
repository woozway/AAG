import sys
import bisect

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    while True:
        try:
            n = next(iterator)
            m = next(iterator)
        except StopIteration:
            break
            
        mchs = [(next(iterator), next(iterator)) for _ in range(n)]
        tasks = [(next(iterator), next(iterator)) for _ in range(m)]
        
        mchs.sort()
        tasks.sort()
        
        ys = []
        cnt = 0
        res = 0
        j = n - 1
        
        for i in range(m - 1, -1, -1):
            x, y = tasks[i]
            
            while j >= 0 and mchs[j][0] >= x:
                bisect.insort(ys, mchs[j][1])
                j -= 1
                
            idx = bisect.bisect_left(ys, y)
            
            if idx < len(ys):
                cnt += 1
                res += 500 * x + 2 * y
                ys.pop(idx)
                
        print(f"{cnt} {res}")

if __name__ == '__main__':
    main()