import sys

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
        
    val_map = {str(i): i for i in range(2, 10)}
    val_map.update({'0': 10, 'A': 1, 'J': 11, 'Q': 12})
    
    closed = [[] for _ in range(14)]
    for i in range(1, 14):
        for j in range(4):
            ch = tokens[(i - 1) * 4 + j][0]
            closed[i].append(val_map.get(ch, 13))
            
    open_counts = [0] * 14
    
    for t in closed[13]:
        while t != 13:
            open_counts[t] += 1
            t = closed[t].pop()
            
    print(sum(1 for i in range(1, 13) if open_counts[i] >= 4))

if __name__ == '__main__':
    main()