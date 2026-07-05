import sys
import math
import random

INF = 1e10

class Point:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.type = t

def dist(a, b):
    if a.type == b.type:
        return INF
    dx = a.x - b.x
    dy = a.y - b.y
    return math.sqrt(dx * dx + dy * dy)

def dfs(points, l, r):
    if l >= r:
        return INF
    
    mid = (l + r) // 2
    mid_x = points[mid].x
    
    res = min(dfs(points, l, mid), dfs(points, mid + 1, r))
    
    temp = [None] * (r - l + 1)
    i, j = l, mid + 1
    k = 0
    while i <= mid and j <= r:
        if points[i].y < points[j].y:
            temp[k] = points[i]
            i += 1
        else:
            temp[k] = points[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = points[i]
        i += 1
        k += 1
    while j <= r:
        temp[k] = points[j]
        j += 1
        k += 1
    
    for i in range(len(temp)):
        points[l + i] = temp[i]
        
    candidates = []
    for i in range(l, r + 1):
        if abs(points[i].x - mid_x) < res:
            candidates.append(points[i])
            
    for i in range(len(candidates)):
        for j in range(i - 1, -1, -1):
            if candidates[i].y - candidates[j].y >= res:
                break
            res = min(res, dist(candidates[i], candidates[j]))
            
    return res

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    T = int(input_data[idx])
    idx += 1
    
    for _ in range(T):
        n = int(input_data[idx])
        idx += 1
        
        points = []
        for i in range(n):
            points.append(Point(float(input_data[idx]), float(input_data[idx + 1]), 0))
            idx += 2
        for i in range(n):
            points.append(Point(float(input_data[idx]), float(input_data[idx + 1]), 1))
            idx += 2
            
        random.shuffle(points)
        points.sort(key=lambda p: p.x)
        
        ans = dfs(points, 0, 2 * n - 1)
        print(f"{ans:.3f}")

if __name__ == '__main__':
    main()