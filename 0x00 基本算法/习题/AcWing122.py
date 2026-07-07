import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n + 1]]
    
    b = sum(a) // n
    c = [0] * n
    
    current_sum = 0
    for i in range(n - 1):
        current_sum += a[i]
        c[i] = (i + 1) * b - current_sum
        
    c.sort()
    median = c[n // 2]
    
    res = sum(abs(x - median) for x in c)
    print(res)

if __name__ == '__main__':
    main()