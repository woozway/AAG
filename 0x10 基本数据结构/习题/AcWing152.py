import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    heights = [0] * (m + 1)
    max_area = 0
    idx = 2
    
    for _ in range(n):
        for j in range(m):
            if input_data[idx] == 'F':
                heights[j] += 1
            else:
                heights[j] = 0
            idx += 1
            
        stack = []
        for i in range(m + 1):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                if h * w > max_area:
                    max_area = h * w
            stack.append(i)
            
    print(max_area * 3)

if __name__ == '__main__':
    main()