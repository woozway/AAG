import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:]]
    
    a.sort()
    
    res = 0
    median = a[n // 2]
    for x in a:
        res += abs(x - median)
        
    print(res)

if __name__ == '__main__':
    main()