import sys

def main():
    s = sys.stdin.read().split()
    if not s:
        return
    
    s = s[0]
    n = len(s)
    
    sa = list(range(n))
    rk = [ord(c) for c in s]
    
    k = 1
    while k < n:
        keys = [(rk[i] << 32) | (rk[i + k] + 1 if i + k < n else 0) for i in range(n)]
        sa.sort(key=keys.__getitem__)
        
        tmp = [0] * n
        r = 0
        tmp[sa[0]] = 0
        for i in range(1, n):
            if keys[sa[i]] != keys[sa[i - 1]]:
                r += 1
            tmp[sa[i]] = r
            
        rk = tmp
        if r == n - 1:
            break
        k <<= 1

    height = [0] * n
    h = 0
    for i in range(n):
        if rk[i] > 0:
            j = sa[rk[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            height[rk[i]] = h
            if h > 0:
                h -= 1

    sys.stdout.write(" ".join(map(str, sa)) + "\n")
    sys.stdout.write(" ".join(map(str, height)) + "\n")

if __name__ == '__main__':
    main()