from heapq import heappush, heappop

q = [] # minHeap
def main():
    n, k = [int(x) for x in input().split()]
    for _ in range(n):
        a = int(input())
        heappush(q, (a, 0))
    while (n - 1) % (k - 1):
        n += 1
        heappush(q, (0, 0))
    
    ans = 0
    while len(q) != 1:
        num, w = 0, 0
        for _ in range(k):
            v = heappop(q)
            num += v[0]
            w = max(w, v[1])
        ans += num
        heappush(q, (num, w + 1))
    print(ans)
    print(q[0][1])
    
main()