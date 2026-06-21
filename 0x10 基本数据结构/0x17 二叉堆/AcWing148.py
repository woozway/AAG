from heapq import heappush, heappop

q = []
def main():
    n = int(input())
    for a in (int(x) for x in input().split()): heappush(q, a)
    ans = 0
    while len(q) != 1:
        x, y = heappop(q), heappop(q)
        ans += x + y
        heappush(q, x + y)
    print(ans)
    
main()