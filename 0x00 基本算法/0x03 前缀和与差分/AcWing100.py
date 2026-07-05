import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [0] * (n + 2)
    for i in range(1, n + 1):
        a[i] = int(input_data[i])
        
    for i in range(n, 1, -1):
        a[i] -= a[i - 1]
        
    pos = 0
    neg = 0
    for i in range(2, n + 1):
        if a[i] > 0:
            pos += a[i]
        else:
            neg -= a[i]
            
    print(min(pos, neg) + abs(pos - neg))
    print(abs(pos - neg) + 1)

if __name__ == '__main__':
    main()