import sys

def check(avg, n, m, cows, sum_arr):
    for i in range(1, n + 1):
        sum_arr[i] = sum_arr[i - 1] + (cows[i] - avg)
    
    mins = 0
    for i in range(m, n + 1):
        mins = min(mins, sum_arr[i - m])
        if sum_arr[i] - mins >= 0:
            return True
    return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    cows = [0] * (n + 1)
    r = 0.0
    for i in range(1, n + 1):
        cows[i] = int(input_data[i + 1])
        r = max(r, float(cows[i]))
        
    l = 0.0
    sum_arr = [0.0] * (n + 1)
    
    while r - l > 1e-5:
        mid = (l + r) / 2
        if check(mid, n, m, cows, sum_arr):
            l = mid
        else:
            r = mid
            
    print(int(r * 1000))

if __name__ == '__main__':
    main()