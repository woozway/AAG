N = 6
a, aa, ans = None, None, 0

def dj(x, y):
    global aa
    aa[x] ^= (1 << y)
    if x != 1: aa[x - 1] ^= (1 << y)
    if x != 5: aa[x + 1] ^= (1 << y)
    if y != 0: aa[x] ^= (1 << (y - 1))
    if y != 4: aa[x] ^= (1 << (y + 1))

def pd(p):
    global aa, ans
    k = 0
    aa = a[:]
    for i in range(5):
        if not ((p >> i) & 1):
            dj(1, i)
            k += 1
            if k >= ans: return
    for x in range(1, 5):
        for y in range(5):
            if not ((aa[x] >> y) & 1):
                dj(x + 1, y)
                k += 1
                if k >= ans: return
    if aa[5] == 31: ans = k
    
def abc():
    global a, ans
    a = [0] * N
    for i in range(1, 6):
        while True:
            s = input().strip()
            if s:
                a[i] = int(s, 2)
                break
    ans = 7
    for p in range(1 << 5): pd(p)
    print(-1 if ans == 7 else ans)

def main():
    n = int(input())
    for _ in range(n):
        abc()
 
main()   