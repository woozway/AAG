from heapq import heappush, heappop
def rd(m):
    v = []
    while len(v) < m:
        v.extend([int(x) for x in input().split()])
    return v
    
def Running_Median():
    q1, q2 = [], []
    num, n = [int(x) for x in input().split()]
    print(num, (n + 1) // 2)
    v = rd(n)
    print(v[0], end='')
    heappush(q2, v[0])
    cnt = 1
    for i in range(2, n + 1):
        a = v[i - 1]
        if a < q2[0]: heappush(q1, -a)
        else: heappush(q2, a)
        s = len(q1)
        if s > i // 2:
            heappush(q2, -heappop(q1))
        if s < i // 2:
            heappush(q1, -heappop(q2))
        if i % 2:
            if cnt % 10: print(' ', end='')
            print(q2[0], end='')
            cnt += 1
            if cnt % 10 == 0: print()
    if cnt % 10: print()

def main():
    t = int(input())
    for _ in range(t): Running_Median()

main()