import sys

def main():
    input_data = map(int, sys.stdin.read().split())
    
    try:
        t = next(input_data)
    except StopIteration:
        return
        
    for _ in range(t):
        p = next(input_data)
        n = next(input_data)
        
        res = sum(pow(next(input_data), next(input_data), p) for _ in range(n)) % p
        print(res)

if __name__ == '__main__':
    main()