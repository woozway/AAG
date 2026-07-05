import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    cows = []
    idx = 1
    for i in range(n):
        w = int(input_data[idx])
        s = int(input_data[idx + 1])
        idx += 2
        cows.append((w + s, w))
        
    cows.sort()
    
    res = -2 * 10**9
    sum_w = 0
    
    for i in range(n):
        s_val = cows[i][0] - cows[i][1]
        w_val = cows[i][1]
        res = max(res, sum_w - s_val)
        sum_w += w_val
        
    print(res)

if __name__ == '__main__':
    main()