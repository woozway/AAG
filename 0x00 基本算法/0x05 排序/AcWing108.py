N = 251010
n, ans, a, c = 0, 0, [[] for _ in range(2)], [0] * N

def merge(k, l, mid, r):
    global ans
    i, j = l, mid + 1
    for p in range(l, r + 1):
        if j > r or (i <= mid and a[k][i] <= a[k][j]): c[p] = a[k][i]; i += 1
        else: ans += mid - i + 1; c[p] = a[k][j]; j += 1
    for p in range(l, r + 1): a[k][p] = c[p]

def mergesort(k, l, r):
    if l == r: return
    mid = (l + r) >> 1
    mergesort(k, l, mid)
    mergesort(k, mid + 1, r)
    merge(k, l, mid, r)

def calc(k):
    global ans
    ans = 0
    mergesort(k, 0, (n * n - 1) - 1)
    return ans

def rd(n):
    return [int(x) for _ in range(n) for x in input().split() if x != '0']
    
def main():
    global n, a
    try:
        while True:
            n = int(input())
            a = rd(n), rd(n)
            print("NIE" if a[0] and (calc(1) - calc(0)) & 1 else "TAK")
    except:
        pass

main()