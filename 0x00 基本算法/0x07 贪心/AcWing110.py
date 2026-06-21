N = 2506
def main():
    c, l = map(int, input().split())
    cow, spf = [0] * N, [0] * N
    for i in range(1, c + 1): cow[i] = list(map(int, input().split()))
    for i in range(1, l + 1): spf[i] = list(map(int, input().split()))
    cow[1 : c + 1] = sorted(cow[1 : c + 1], key=lambda x: x[0], reverse=True)
    spf[1 : l + 1] = sorted(spf[1 : l + 1], key=lambda x: x[0], reverse=True)
    ans = 0
    for i in range(1, c + 1):
        for j in range(1, l + 1):
            if spf[j][1] and spf[j][0] >= cow[i][0] and spf[j][0] <= cow[i][1]:
                ans += 1
                spf[j][1] -= 1
                break
    print(ans)
    
main()