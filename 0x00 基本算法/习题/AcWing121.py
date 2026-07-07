import sys
import bisect

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    try:
        c = next(iterator)
        n = next(iterator)
    except StopIteration:
        return
        
    points = []
    nums_set = {0}
    
    for _ in range(n):
        x = next(iterator)
        y = next(iterator)
        points.append((x, y))
        nums_set.add(x)
        nums_set.add(y)
        
    numbers = sorted(list(nums_set))
    num_len = len(numbers)
    
    prefix_sum = [[0] * num_len for _ in range(num_len)]
    
    for x, y in points:
        idx_x = bisect.bisect_left(numbers, x)
        idx_y = bisect.bisect_left(numbers, y)
        prefix_sum[idx_x][idx_y] += 1
        
    for i in range(1, num_len):
        for j in range(1, num_len):
            prefix_sum[i][j] += (prefix_sum[i - 1][j] + 
                                 prefix_sum[i][j - 1] - 
                                 prefix_sum[i - 1][j - 1])
            
    def check(length):
        x1 = 1
        for x2 in range(1, num_len):
            while numbers[x2] - numbers[x1] + 1 > length:
                x1 += 1
            y1 = 1
            for y2 in range(1, num_len):
                while numbers[y2] - numbers[y1] + 1 > length:
                    y1 += 1
                
                count = (prefix_sum[x2][y2] - 
                         prefix_sum[x1 - 1][y2] - 
                         prefix_sum[x2][y1 - 1] + 
                         prefix_sum[x1 - 1][y1 - 1])
                if count >= c:
                    return True
        return False

    l, r = 1, 10000
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
            
    print(l)

if __name__ == '__main__':
    main()