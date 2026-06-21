import math
N = 15
d, f = [math.inf] * N, [math.inf] * N

def main():
    n = 12
    d[1] = f[1] = 1
    for i in range(2, n + 1): d[i] = 2 * d[i - 1] + 1
    for i in range(2, n + 1):
        for j in range(1, i):
            f[i] = min(f[i], 2 * f[j] + d[i - j])
    for i in range(1, n + 1):
        print(f[i])
        
main()