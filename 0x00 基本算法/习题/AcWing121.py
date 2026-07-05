import sys
import bisect

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    C = int(input_data[0])
    n = int(input_data[1])
    
    points = []
    numbers = [0]
    idx = 2
    for i in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx += 2
        points.append((x, y))
        numbers.append(x)
        numbers.append(y)
        
    numbers = sorted(list(set(numbers)))
    
    m = len(numbers)
    sum_mat = [[0 for _ in range(m)] for _ in range(m)]
    
    def find(val):
        return bisect.bisect_left(numbers, val)
        
    for x, y in points:
        sum_mat[find(x)][find(y)] += 1
        
    for i in range(1, m):
        for j in range(1, m):
            sum_mat[i][j] += sum_mat[i-1][j] + sum_mat[i][j-1] - sum_mat[i-1][j-1]
            
    def check(length):
        x1 = 1
        for x2 in range(1, m):
            while numbers[x2] - numbers[x1] + 1 > length:
                x1 += 1
            y1 = 1
            for y2 in range(1, m):
                while numbers[y2] - numbers[y1] + 1 > length:
                    y1 += 1
                val = sum_mat[x2][y2] - sum_mat[x1-1][y2] - sum_mat[x2][y1-1] + sum_mat[x1-1][y1-1]
                if val >= C:
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