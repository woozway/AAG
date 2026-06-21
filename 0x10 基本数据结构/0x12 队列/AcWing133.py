from math import inf
N, M = 100010, 7000010
n, m, q, u, v, t, delta = 0, 0, 0, 0, 0, 0, 0
q1, q2, q3, hh1, hh2, hh3, tt1, tt2, tt3 = [0] * N, [0] * M, [0] * M, 0, 0, 0, -1, -1, -1

def max3():
    global n, m, q, u, v, t, delta, hh1, hh2, hh3, tt1, tt2, tt3
    x = -inf
    if hh1 <= tt1: x = max(x, q1[hh1])
    if hh2 <= tt2: x = max(x, q2[hh2])
    if hh3 <= tt3: x = max(x, q3[hh3])
    if hh1 <= tt1 and x == q1[hh1]: hh1 += 1
    elif hh2 <= tt2 and x == q2[hh2]: hh2 += 1
    else: hh3 += 1
    return x
    
def main():
    global n, m, q, u, v, t, delta, hh1, hh2, hh3, tt1, tt2, tt3
    n, m, q, u, v, t = map(int, input().split())
    q1[:n] = [int(x) for x in input().split()]
    q1[:n] = sorted(q1[:n], reverse=True)
    tt1 = n - 1
    for i in range(1, m + 1):
        x = max3()
        x += delta
        left = x * u // v
        right = x - left
        if i % t == 0: print("%d " %x, end='')
        delta += q
        tt2 += 1; q2[tt2] = left - delta
        tt3 += 1; q3[tt3] = right - delta
    print()
    for i in range(1, n + m + 1):
        x = max3()
        if i % t == 0: print("%d " %(x+delta), end='')
    print()

main()