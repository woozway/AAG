N = 100006
n, tot, P = 0, 0, 99991
a, snow, head, nxt = [0] * 6, [0] * N, [0] * N, [0] * N
def H(a):
    global n, tot, P
    sum_, mul_ = 0, 1
    for i in range(6):
        sum_ = (sum_ + a[i]) % P
        mul_ = mul_ * a[i] % P
    return (sum_ + mul_) % P
    
def equal(a, b):
    global n, tot, P
    for i in range(6):
        for j in range(6):
            eq = 1
            for k in range(6):
                if a[(i + k) % 6] != b[(j + k) % 6]:
                    eq = 0
                    break
            if eq: return 1
            eq = 1
            for k in range(6):
                if a[(i + k) % 6] != b[(j - k + 6) % 6]:
                    eq = 0
                    break
            if eq: return 1
    return 0
    
def insert(a):
    global n, tot, P
    val = H(a)
    i = head[val]
    while i:
        if equal(snow[i], a): return 1
        i = nxt[i]
    tot += 1
    snow[tot] = a[:]
    nxt[tot] = head[val]
    head[val] = tot
    return 0
    
def main():
    global n, tot, P
    n = int(input())
    for i in range(1, n + 1):
        a[:6] = [int(x) for x in input().split()]
        if insert(a):
            print("Twin snowflakes found.")
            return
    print("No two snowflakes are alike.")
    
main()