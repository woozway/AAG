import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    grid = input_data[2:n + 2]
    
    width = m
    for w in range(1, m + 1):
        if all(row[w:] == row[:-w] for row in grid):
            width = w
            break
            
    short_grid = [row[:width] for row in grid]
    
    ne = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and short_grid[i] != short_grid[j]:
            j = ne[j - 1]
        if short_grid[i] == short_grid[j]:
            j += 1
        ne[i] = j
        
    height = n - ne[-1] if n > 0 else 0
    
    print(width * height)

if __name__ == '__main__':
    main()