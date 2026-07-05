import sys

def mul(A, b):
    C = []
    t = 0
    i = 0
    while i < len(A) or t:
        if i < len(A):
            t += A[i] * b
        C.append(t % 10)
        t //= 10
        i += 1
    while len(C) > 1 and C[-1] == 0:
        C.pop()
    return C

def div(A, b):
    C = []
    r = 0
    for i in range(len(A) - 1, -1, -1):
        r = r * 10 + A[i]
        C.append(r // b)
        r %= b
    C.reverse()
    while len(C) > 1 and C[-1] == 0:
        C.pop()
    return C

def max_vec(A, B):
    if len(A) > len(B):
        return A
    if len(A) < len(B):
        return B
    for i in range(len(A) - 1, -1, -1):
        if A[i] > B[i]:
            return A
        if A[i] < B[i]:
            return B
    return A

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    p = []
    idx = 1
    for i in range(n + 1):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        p.append((a * b, a))
        idx += 2
        
    p_king = p[0]
    p_ministers = sorted(p[1:])
    p = [p_king] + p_ministers
    
    product = [1]
    res = [0]
    
    for i in range(n + 1):
        if i > 0:
            val = div(product, p[i][0] // p[i][1])
            res = max_vec(res, val)
        product = mul(product, p[i][1])
        
    print("".join(map(str, res[::-1])))

if __name__ == '__main__':
    main()