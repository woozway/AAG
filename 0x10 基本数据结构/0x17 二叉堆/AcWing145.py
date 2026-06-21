from heapq import heappush, heappop
N = 10006
n, a, q = 0, [[0] * 2 for _ in range(N)], []
    
def rd(t):
    global n
    while len(t) < 2 * n: t.extend([int(x) for x in input().split()])
    for i in range(1, n + 1): a[i] = t[2 * (i - 1) + 1], t[2 * (i - 1)]
    
def Supermarket(t):
    global n
    n = t[0]; rd(t[1:])
    a[1 : n + 1] = sorted(a[1 : n + 1], key=lambda x: x[0])
    for i in range(1, n + 1):
        if a[i][0] == len(q) and q[0] < a[i][1]:
            heappop(q)
            heappush(q, a[i][1])
            continue
        if a[i][0] > len(q): heappush(q, a[i][1])
    ans = 0
    while q:
        ans += q[0]
        heappop(q)
    print(ans)

def main():
    while True:
        try:
            line = input()
            if line.strip() == "": continue
            Supermarket([int(x) for x in line.split()])
        except EOFError:
            break

main()