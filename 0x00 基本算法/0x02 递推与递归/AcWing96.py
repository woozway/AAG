import sys

def main():
    n = 12
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        d[i] = d[i - 1] + 1 + d[i - 1]

    f = [0x3f3f3f3f] * (n + 1)
    f[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            f[i] = min(f[i], f[j] + d[i - j] + f[j])

    for i in range(1, n + 1):
        print(f[i])

if __name__ == '__main__':
    main()