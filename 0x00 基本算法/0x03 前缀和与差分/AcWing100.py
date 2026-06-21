N = 100006
a, b = [0] * N, [0] * N

def main():
    n = int(input())
    for i in range(1, n + 1): a[i] = int(input())
    b[n + 1] = 0; b[1] = a[1]
    for i in range(2, n + 1): b[i] = a[i] - a[i - 1]
    p, q = 0, 0
    for i in range(2, n + 1):
        if b[i] > 0: p += b[i]
        elif b[i] < 0: q -= b[i]
    print(max(p, q))
    print(abs(p - q) + 1)

main()