import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = [(int(val), i) for i, val in enumerate(input_data[1:n + 1])]
    
    a.sort()
    
    res = 1
    last = n + 1
    direction = -1
    i = 0
    
    while i < n:
        j = i
        while j < n and a[j][0] == a[i][0]:
            j += 1
            
        minx = a[i][1]
        maxx = a[j - 1][1]
        
        if direction == -1:
            if last > maxx:
                last = minx
            else:
                direction = 1
                last = maxx
        else:
            if last < minx:
                last = maxx
            else:
                res += 1
                last = minx
                direction = -1
                
        i = j
        
    print(res)

if __name__ == '__main__':
    main()