import sys

def work(q):
    q.sort()
    mid = q[len(q) // 2]
    return sum(abs(v - mid) for v in q)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    x = [int(input_data[i]) for i in range(1, 2 * n, 2)]
    y = [int(input_data[i]) for i in range(2, 2 * n + 1, 2)]
    
    x = [val - i for i, val in enumerate(sorted(x))]
    
    print(work(x) + work(y))

if __name__ == '__main__':
    main()