from math import inf
a, b, s = [0] * 100001, [0] * 100001, [0] * 100001
def main():
    N, L = [int(x) for x in input().split()]
    for i in range(1, N + 1): a[i] = int(input())
    eps = 1e-5
    l, r = 1, 1e6
    while r - l > eps:
        mid = (l + r) / 2
        for i in range(1, N + 1): b[i] = a[i] - mid
        for i in range(1, N + 1): s[i] = s[i - 1] + b[i]
        ans, min_val = -inf, inf
        for i in range(L, N + 1):
            min_val = min(min_val, s[i - L])
            ans = max(ans, s[i] - min_val)
        if ans >= 0: l = mid
        else: r = mid
    print(int(r * 1000))
    
main()