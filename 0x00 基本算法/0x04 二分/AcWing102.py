import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    cows = [int(x) for x in input_data[2:n + 2]]
    
    def check(avg):
        sums = [0.0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + cows[i] - avg
            
        min_s = 0.0
        for i in range(m, n + 1):
            if sums[i - m] < min_s:
                min_s = sums[i - m]
            if sums[i] >= min_s:
                return True
        return False

    l = 0.0
    r = float(max(cows)) if cows else 0.0
    
    while r - l > 1e-5:
        mid = (l + r) / 2.0
        if check(mid):
            l = mid
        else:
            r = mid
            
    print(int(r * 1000))

if __name__ == '__main__':
    main()