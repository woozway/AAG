N = 500006
n, ans, a, b = 0, 0, [0] * N, [0] * N

def merge(l, mid, r):
    global ans
    if l == r: return
    merge(l, (l + mid) >> 1, mid)
    merge(mid + 1, (mid + 1 + r) >> 1, r)
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if j > r or (i <= mid and a[i] <= a[j]): b[k] = a[i]; i += 1
        else: b[k] = a[j]; j += 1; ans += mid - i + 1
    for k in range(l, r + 1): a[k] = b[k]

def Ultra_QuickSort():
    global ans
    for i in range(1, n + 1): a[i] = int(input())
    ans = 0
    merge(1, (1 + n) >> 1, n)
    print(ans)
    
def main():
    global n
    while True:
        n = int(input())
        if n == 0: break
        Ultra_QuickSort()

main()