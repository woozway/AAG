import sys
import math
import random

def main():
    sys.setrecursionlimit(2000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    try:
        T = int(next(iterator))
    except StopIteration:
        return
        
    for _ in range(T):
        n = int(next(iterator))
        points = []
        
        for _ in range(n):
            points.append((float(next(iterator)), float(next(iterator)), 0))
            
        for _ in range(n):
            points.append((float(next(iterator)), float(next(iterator)), 1))
            
        random.shuffle(points)
        points.sort(key=lambda p: p[0])
        
        def dist(p1, p2):
            if p1[2] == p2[2]:
                return float('inf')
            return math.hypot(p1[0] - p2[0], p1[1] - p2[1])
            
        def dfs(l, r):
            if l >= r:
                return float('inf')
                
            mid = (l + r) // 2
            mid_x = points[mid][0]
            
            res = min(dfs(l, mid), dfs(mid + 1, r))
            
            left = points[l:mid + 1]
            right = points[mid + 1:r + 1]
            merged = []
            i = 0
            j = 0
            len_left = len(left)
            len_right = len(right)
            
            while i < len_left and j < len_right:
                if left[i][1] < right[j][1]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            points[l:r + 1] = merged
            
            temp = [p for p in merged if mid_x - res <= p[0] <= mid_x + res]
            
            for i in range(len(temp)):
                for j in range(i - 1, -1, -1):
                    if temp[i][1] - temp[j][1] >= res:
                        break
                    res = min(res, dist(temp[i], temp[j]))
                    
            return res

        ans = dfs(0, 2 * n - 1)
        print(f"{ans:.3f}")

if __name__ == '__main__':
    main()