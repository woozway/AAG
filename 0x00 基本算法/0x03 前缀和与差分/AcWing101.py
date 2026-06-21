N = 10006
c, d = [0] * N, [0] * N
existed = set()

def main():
    n, p, h, m = [int(x) for x in input().split()]
    for _ in range(m):
        a, b = [int(x) for x in input().split()]
        if a > b: a, b = b, a
        if (a, b) in existed: continue
        d[a + 1] -= 1; d[b] += 1
        existed.add((a, b))
    for i in range(1, n + 1):
        c[i] = c[i - 1] + d[i]
        print(h + c[i])
        
main()