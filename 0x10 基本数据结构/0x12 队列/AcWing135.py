from math import inf

N = 300006
q, s = [0] * N, [0] * N
def main():
    n, m = [int(x) for x in input().split()]
    s[1 : n + 1] = [int(x) for x in input().split()]
    for i in range(1, n + 1): s[i] += s[i - 1]
    ans, l, r = -inf, 1, 1
    q[l] = 0
    for i in range(1, n + 1):
        while l <= r and q[l] < i - m: l += 1
        ans = max(ans, s[i] - s[q[l]])
        while l <= r and s[q[r]] >= s[i]: r -= 1
        r += 1; q[r] = i
    print(ans)
    
main()