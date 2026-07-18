import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    out = []
    
    while idx < len(input_data):
        n = int(input_data[idx])
        if n == 0:
            break
        idx += 1
        
        h = [-1] + [int(x) for x in input_data[idx : idx + n]] + [-1]
        idx += n
        
        l = [0] * (n + 2)
        r = [0] * (n + 2)
        
        q = [0]
        for i in range(1, n + 1):
            while h[i] <= h[q[-1]]:
                q.pop()
            l[i] = q[-1]
            q.append(i)
            
        q = [n + 1]
        for i in range(n, 0, -1):
            while h[i] <= h[q[-1]]:
                q.pop()
            r[i] = q[-1]
            q.append(i)
            
        res = max(h[i] * (r[i] - l[i] - 1) for i in range(1, n + 1))
        out.append(str(res))
        
    if out:
        print('\n'.join(out))

if __name__ == '__main__':
    main()