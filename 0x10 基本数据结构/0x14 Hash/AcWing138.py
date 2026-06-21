N = 1000010
M = 10 ** 9 + 7
s, f, p = [0] * N, [0] * N, [0] * N

def rd():
    lrs = []
    while len(lrs) < 4:
        lrs.extend(map(int, input().split()))
    return lrs

def main():
    s[1:] = list(input())
    n = len(s[1:])
    p[0] = 1
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * 131 + (ord(s[i]) - ord('a') + 1)) % M
        p[i] = p[i - 1] * 131 % M
    m = int(input())
    for _ in range(m):
        l1, r1, l2, r2 = rd()
        if (f[r1] - f[l1 - 1] * p[r1 - l1 + 1]) % M == (f[r2] - f[l2 - 1] * p[r2 - l2 + 1]) % M:
            print("Yes")
        else:
            print("No")
            
main()