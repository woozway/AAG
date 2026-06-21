def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n - 1):
        ans += max(a[i+1] - a[i], 0)
    print(ans)

main()