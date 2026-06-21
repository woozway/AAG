from heapq import heappush, heappop
N = 50006
def main():
    n = int(input())
    cow, ans, s = [0] * N, [0] * N, [], 
    for i in range(1, n + 1):
        l, r = map(int, input().split())
        cow[i] = [i, l, r, 0]
    cow[1 : n + 1] = sorted(cow[1 : n + 1], key=lambda x: x[1])
    for i in range(1, n + 1):
        num = len(s)
        if num and s[0][0] < cow[i][1]:
            cow[i][3] = s[0][1]
            heappop(s)
            heappush(s, [cow[i][2], cow[i][3]])
            continue
        num += 1; cow[i][3] = num
        heappush(s, [cow[i][2], num])
    print(len(s))
    for i in range(1, n + 1): ans[cow[i][0]] = cow[i][3]
    for i in range(1, n + 1): print(ans[i])
    
main()