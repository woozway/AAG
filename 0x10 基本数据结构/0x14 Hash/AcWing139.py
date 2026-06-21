N, P, M = 1000006, 131, 1 << 32 # MOD
f1, f2, p = [0] * N, [0] * N, [0] * N

def H1(i, j):
    return (f1[j] - f1[i - 1] * p[j - i + 1]) % M
    
def H2(i, j):
    return (f2[i] - f2[j + 1] * p[j - i + 1]) % M
    
def main():
    id_ = 0
    p[0] = 1
    for i in range(1, N): p[i] = (p[i - 1] * P) % M
    while True:
        s = input()
        if s == 'END': break
        s = [0] + list(s)
        ans, len_ = 0, len(s[1:])
        f1[0], f2[len_ + 1] = 0, 0
        for i in range(1, len_ + 1): f1[i] = (f1[i - 1] * P + ord(s[i])) % M
        for i in range(len_, 0, -1): f2[i] = (f2[i + 1] * P + ord(s[i])) % M
        for i in range(1, len_ + 1):
            l, r = 0, min(i - 1, len_ - i)
            while l < r:
                mid = (l + r + 1) >> 1
                if H1(i-mid, i) == H2(i, i + mid): l = mid
                else: r = mid - 1
            ans = max(l * 2 + 1, ans)
            l, r = 0, min(i - 1, len_ - i + 1)
            while l < r:
                mid = (l + r + 1) >> 1
                if H1(i - mid, i - 1) == H2(i, i + mid - 1): l = mid
                else: r = mid - 1
            ans = max(l * 2, ans)
        id_ += 1
        print("Case %d: %d" %(id_, ans))

main()