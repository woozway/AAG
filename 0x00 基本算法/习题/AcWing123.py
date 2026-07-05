import sys

def work(q, n):
    q.sort()
    res = 0
    median = q[n // 2]
    for val in q:
        res += abs(val - median)
    return res

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x = [0] * n
    y = [0] * n
    
    idx = 1
    for i in range(n):
        x[i] = int(input_data[idx])
        y[i] = int(input_data[idx + 1])
        idx += 2
        
    x.sort()
    for i in range(n):
        x[i] -= i
        
    print(work(x, n) + work(y, n))

if __name__ == '__main__':
    main()