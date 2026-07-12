import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return
        
    stkl = []
    stkr = []
    sums = [0]
    f = [-float('inf')]
    
    out = []
    
    for _ in range(n):
        op = next(iterator)
        if op == 'I':
            x = int(next(iterator))
            stkl.append(x)
            sums.append(sums[-1] + x)
            f.append(max(f[-1], sums[-1]))
        elif op == 'D':
            if stkl:
                stkl.pop()
                sums.pop()
                f.pop()
        elif op == 'L':
            if stkl:
                stkr.append(stkl.pop())
                sums.pop()
                f.pop()
        elif op == 'R':
            if stkr:
                x = stkr.pop()
                stkl.append(x)
                sums.append(sums[-1] + x)
                f.append(max(f[-1], sums[-1]))
        elif op == 'Q':
            k = int(next(iterator))
            out.append(str(f[k]))
            
    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()