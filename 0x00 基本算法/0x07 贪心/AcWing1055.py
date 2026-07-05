import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    p = [int(x) for x in input_data[1:]]
    
    res = 0
    for i in range(n - 1):
        res += max(0, p[i + 1] - p[i])
        
    print(res)

if __name__ == '__main__':
    main()