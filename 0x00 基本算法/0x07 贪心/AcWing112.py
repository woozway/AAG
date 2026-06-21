from math import inf, sqrt
N = 1006
n, d, p = 0, 0, [[0] * 4 for _ in range(N)] # p[i]=[x,y,l,r]
def Radar_Installation():
    global n, d, p
    for i in range(1, n + 1): p[i][:2] = list(map(int, input().split()))
    b = True
    for i in range(1, n + 1):
        if p[i][1] > d:
            b = False
            break
    if not b:
        print("-1")
        return
    for i in range(1, n + 1):
        k = sqrt(d ** 2 - p[i][1] ** 2)
        p[i][2:] = p[i][0] - k, p[i][0] + k
    p[1 : n + 1] = sorted(p[1 : n + 1], key=lambda x: x[2])
    ans = 0
    pos = -inf
    for i in range(1, n + 1):
        if pos < p[i][2]:
            ans += 1
            pos = p[i][3]
        else:
            pos = min(p[i][3], pos)
    print(ans)

def main():
    global n, d
    n, d = map(int, input().split())
    Radar_Installation()

main()