import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n + 1]]
    
    diffs = [y - x for x, y in zip(a, a[1:])]
    
    pos = sum(d for d in diffs if d > 0)
    neg = sum(-d for d in diffs if d < 0)
    
    print(max(pos, neg))
    print(abs(pos - neg) + 1)

if __name__ == '__main__':
    main()