import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = sorted(int(x) for x in input_data[1:n + 1])
    
    median = a[n // 2]
    res = sum(abs(x - median) for x in a)
    
    print(res)

if __name__ == '__main__':
    main()