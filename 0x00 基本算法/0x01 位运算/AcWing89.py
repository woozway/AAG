import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    a, b, p = map(int, input_data[:3])
    
    print(pow(a, b, p))

if __name__ == '__main__':
    main()