import sys
import heapq
import bisect
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    
    waits = deque()
    runs = [(-1, 1), (n, 1)]
    endts = []
    tm_ = 0
    cnt = 0

    def give(t, m, p):
        for i in range(len(runs) - 1):
            it_start, it_len = runs[i]
            jt_start = runs[i + 1][0]
            
            if m <= jt_start - (it_start + it_len):
                new_start = it_start + it_len
                runs.insert(i + 1, (new_start, m))
                heapq.heappush(endts, (t + p, new_start))
                return True
        return False

    def finish(t):
        nonlocal tm_
        while endts and endts[0][0] <= t:
            f = endts[0][0]
            
            while endts and endts[0][0] == f:
                _, start = heapq.heappop(endts)
                idx = bisect.bisect_left(runs, (start, 0))
                if idx < len(runs) and runs[idx][0] == start:
                    runs.pop(idx)
            
            tm_ = f
            
            while waits:
                front_m, front_p = waits[0]
                if give(f, front_m, front_p):
                    waits.popleft()
                else:
                    break

    while True:
        try:
            t = int(next(iterator))
            m = int(next(iterator))
            p = int(next(iterator))
        except StopIteration:
            break
            
        if t == 0 and m == 0 and p == 0:
            break
            
        finish(t)
        if not give(t, m, p):
            waits.append((m, p))
            cnt += 1
            
    finish(int(2e9))
    
    print(tm_)
    print(cnt)

if __name__ == '__main__':
    solve()