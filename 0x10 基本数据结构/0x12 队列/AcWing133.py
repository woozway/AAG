import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    q = int(input_data[2])
    u = int(input_data[3])
    v = int(input_data[4])
    t = int(input_data[5])
    
    q1 = sorted([int(x) for x in input_data[6:6+n]], reverse=True)
    q2 = [0] * m
    q3 = [0] * m
    
    h1 = h2 = h3 = 0
    t2 = t3 = 0
    delta = 0
    
    out1 = []
    INF = float('inf')
    
    for i in range(1, m + 1):
        v1 = q1[h1] if h1 < n else -INF
        v2 = q2[h2] if h2 < t2 else -INF
        v3 = q3[h3] if h3 < t3 else -INF
        
        if v1 >= v2 and v1 >= v3:
            x = v1
            h1 += 1
        elif v2 >= v1 and v2 >= v3:
            x = v2
            h2 += 1
        else:
            x = v3
            h3 += 1
            
        x += delta
        if i % t == 0:
            out1.append(str(x))
            
        left = x * u // v
        right = x - left
        delta += q
        
        q2[t2] = left - delta
        t2 += 1
        q3[t3] = right - delta
        t3 += 1
        
    print(" ".join(out1))
    
    out2 = []
    for i in range(1, n + m + 1):
        v1 = q1[h1] if h1 < n else -INF
        v2 = q2[h2] if h2 < t2 else -INF
        v3 = q3[h3] if h3 < t3 else -INF
        
        if v1 >= v2 and v1 >= v3:
            x = v1
            h1 += 1
        elif v2 >= v1 and v2 >= v3:
            x = v2
            h2 += 1
        else:
            x = v3
            h3 += 1
            
        if i % t == 0:
            out2.append(str(x + delta))
            
    print(" ".join(out2))

if __name__ == '__main__':
    main()