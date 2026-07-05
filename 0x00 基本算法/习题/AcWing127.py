import sys
from bisect import bisect_left

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        
        mchs = []
        for i in range(n):
            mchs.append((int(input_data[idx]), int(input_data[idx + 1])))
            idx += 2
            
        tasks = []
        for i in range(m):
            tasks.append((int(input_data[idx]), int(input_data[idx + 1])))
            idx += 2
            
        mchs.sort()
        tasks.sort()
        
        ys = []
        cnt = 0
        res = 0
        
        j = n - 1
        for i in range(m - 1, -1, -1):
            x, y = tasks[i]
            while j >= 0 and mchs[j][0] >= x:
                ys.append(mchs[j][1])
                j -= 1
            
            ys.sort()
            pos = bisect_left(ys, y)
            
            if pos < len(ys):
                cnt += 1
                res += 500 * x + 2 * y
                ys.pop(pos)
                
        print(f"{cnt} {res}")

if __name__ == '__main__':
    main()