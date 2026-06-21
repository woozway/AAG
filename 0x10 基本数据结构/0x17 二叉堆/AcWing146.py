from heapq import heappush, heappop
N = 2006
m, n = 0, 0
a, b, c = [0] * N, [0] * N, [0] * N

def merge():
    q = []
    for i in range(1, n + 1): heappush(q, (a[1] + b[i], 1))
    for i in range(1, n + 1):
        s, p = heappop(q)
        c[i] = s
        heappush(q, (s - a[p] + a[p + 1], p + 1))
    for i in range(1, n + 1): a[i] = c[i]
    
def Sequence():
    global m, n
    m, n = [int(x) for x in input().split()]
    a[1 : n + 1] = sorted([int(x) for x in input().split()])
    for _ in range(m - 1):
        b[1 : n + 1] = [int(x) for x in input().split()]
        merge()
    for i in range(1, n+1): print("%d " %a[i], end='')
    print()
    
def main():
    t = int(input())
    for _ in range(t): Sequence()
    
main()