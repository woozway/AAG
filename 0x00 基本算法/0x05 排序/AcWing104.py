N = 100006
a = [0] * N
def main():
    n = int(input())
    a[1:] = [int(x) for x in input().split()]
    a[1:] = sorted(a[1:])
    ans = 0
    for i in range(1, n // 2 + 1):
        ans += a[n - i + 1] - a[i]
    print(ans)
    
main()