import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n_orig, m = int(input_data[0]), int(input_data[1])
    
    a = [0, 0]
    for x in map(int, input_data[2:2 + n_orig]):
        if a[-1] * x < 0:
            a.append(x)
        else:
            a[-1] += x
            
    n = len(a) - 1
    a.append(0)
    
    cnt = 0
    res = 0
    for i in range(1, n + 1):
        if a[i] > 0:
            cnt += 1
            res += a[i]
            
    l = [0] * (n + 2)
    r = [0] * (n + 2)
    st = [False] * (n + 2)
    
    heap = []
    for i in range(1, n + 1):
        l[i] = i - 1
        r[i] = i + 1
        heapq.heappush(heap, (abs(a[i]), i))
        
    def remove(p):
        l[r[p]] = l[p]
        r[l[p]] = r[p]
        st[p] = True

    while cnt > m:
        while heap and st[heap[0][1]]:
            heapq.heappop(heap)
            
        if not heap:
            break
            
        v, p = heapq.heappop(heap)
        
        if (l[p] != 0 and r[p] != n + 1) or a[p] > 0:
            cnt -= 1
            res -= v
            
            left = l[p]
            right = r[p]
            
            a[p] += a[left] + a[right]
            heapq.heappush(heap, (abs(a[p]), p))
            
            remove(left)
            remove(right)
            
    print(res)

if __name__ == '__main__':
    solve()