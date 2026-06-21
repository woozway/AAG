N = 100006
n, p, ans, a, s, w, rest = 0, 0, 0, [0] * N, [0] * N, [0] * N, []

def Largest():
    global n, p, ans, a, s, w, rest
    a[1 : n + 1] = rest
    a[n + 1] = p = 0
    ans = 0
    for i in range(1, n + 2):
        if a[i] > s[p]:
            p += 1; s[p] = a[i]; w[p] = 1
        else:
            width = 0
            while s[p] > a[i]:
                width += w[p]
                ans = max(ans, width * s[p])
                p -= 1
            p += 1; s[p] = a[i]; w[p] = width + 1
    print(ans)
  
def main():
    global n, p, ans, a, s, w, rest
    while True:
        n, *rest = [int(x) for x in input().split()]
        if n == 0: break
        Largest()
        
main()