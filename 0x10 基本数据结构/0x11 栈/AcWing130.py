# from math import factorial

# def comb(n, k):
#     return factorial(n) // (factorial(k)*factorial(n-k))

# def main():
#     n = int(input())
#     print(comb(2*n, n)//(n+1))
    
# main()

N = 60005
n, tot, pows, p, v = 0, 0, [0] * (2 * N), [0] * (2 * N), [0] * (2 * N)

def fac(n, p):
    cnt = 0
    while n:
        cnt += n // p
        n //= p
    return cnt
    
def gj(a, b):
    c = 0
    for i in range(len(a)):
        a[i] = a[i] * b + c
        c = a[i] // 100000000
        a[i] %= 100000000
    while c:
        a.append(c % 100000000)
        c //= 100000000

def main():
    global n, tot, pows, p, v
    n = int(input())
    for i in range(2, 2 * n + 1):
        if not v[i]:
            p[tot] = i; tot += 1
            for j in range(i * 2, 2 * n + 1, i): v[j] = 1
    for i in range(tot):
        pows[p[i]] = fac(n * 2, p[i]) - fac(n, p[i]) - fac(n + 1, p[i])
    ans = [1]
    for i in range(tot):
        for j in range(pows[p[i]]):
            gj(ans, p[i])
    print(ans[-1], end='')
    for i in range(len(ans) - 2, -1, -1): print("{:08d}".format(ans[i]), end='')
    
main()