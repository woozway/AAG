N = 5006
s = [[0]*N for _ in range(N)]
n, r = [int(x) for x in input().split()]
for _ in range(n):
    x, y, w = [int(x) for x in input().split()]
    s[x][y] += w

for i in range(5001):
    for j in range(5001):
        if not i and not j: continue
        elif not i: s[i][j] += s[i][j - 1]
        elif not j: s[i][j] += s[i - 1][j]
        else: s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]

def main():
    if r > 5000:
        print(s[5000][5000])
        return
    ans = 0
    for i in range(r - 1, 5001):
        for j in range(r - 1, 5001):
            if i == r - 1 and j == r - 1: ans = max(ans, s[i][j])
            elif i == r - 1: ans = max(ans, s[i][j] - s[i][j - r])
            elif j == r - 1: ans = max(ans, s[i][j] - s[i - r][j])
            else: ans = max(ans, s[i][j] - s[i - r][j] - s[i][j - r] + s[i - r][j - r])
    print(ans)
    
main()