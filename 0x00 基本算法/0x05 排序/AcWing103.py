from bisect import bisect_left
N = 200006
a, x, y, cinema, ans = [0] * N, [0] * N, [0] * N, [0] * N * 3, [0] * N * 3
tot, k = 0, 0

def find(f):
    global cinema, k
    return bisect_left(cinema, f, 1, k + 1)

def main():
    global cinema, tot, k
    n = int(input())
    a[1:] = [int(x) for x in input().split()]
    for i in range(1, n + 1):
        tot += 1; cinema[tot] = a[i]
    m = int(input())
    x[1:] = [int(x) for x in input().split()]
    for i in range(1, m + 1):
        tot += 1; cinema[tot] = x[i]
    y[1:] = [int(x) for x in input().split()]
    for i in range(1, m + 1):
        tot += 1; cinema[tot] = y[i]
    cinema[1:] = sorted(set(cinema[1 : tot + 1]))
    k = len(cinema[1:])
    for i in range(1, n + 1): ans[find(a[i])] += 1
    ans0, ans1, ans2 = 1, 0, 0
    for i in range(1, m + 1):
        ansx, ansy = ans[find(x[i])], ans[find(y[i])]
        if ansx > ans1 or (ansx == ans1 and ansy > ans2):
            ans0, ans1, ans2 = i, ansx, ansy
    print(ans0)
    
main()