from math import sqrt
P = 9901
w = []

def ksm(a, b):
    return pow(a, b, P)

def get_sum(p, c):
    if not p: return 0
    if not c: return 1
    if c & 1: return (1 + ksm(p, (c + 1) // 2)) * get_sum(p, (c - 1) // 2) % P
    return ((1 + ksm(p, c // 2)) * get_sum(p, c // 2 - 1) + ksm(p, c)) % P

def fj(a):
    sqrt_a = int(sqrt(a))
    for i in range(2, sqrt_a + 1):
        if not (a % i):
            num = 0
            while not (a % i):
                num += 1
                a //= i
            w.append((i, num))
    if a != 1: w.append((a, 1))

def main():
    a, b = [int(x) for x in input().split()]
    fj(a)
    ans = 1
    for i in range(len(w)):
        p, c = w[i]
        ans = ans * get_sum(p, b * c) % P
    print(ans)

main()