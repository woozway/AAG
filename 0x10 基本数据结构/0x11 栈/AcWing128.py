from math import inf
N = 1000006
st1, st2, s, f = [0] * N, [0] * N, [0] * N, [0] * N

def Editor(q):
    t1, t2 = 0, 0
    for _ in range(q):
        c = input().split()
        if c[0] == 'I':
            t1 += 1; st1[t1] = int(c[1])
            s[t1] = s[t1 - 1] + st1[t1]
            f[t1] = max(f[t1 - 1], s[t1])
            continue
        elif c[0] == 'D':
            if t1: t1 -= 1
            continue
        elif c[0] == 'L':
            if t1: t2 += 1; st2[t2] = st1[t1]; t1 -= 1
            continue
        elif c[0] == 'R':
            if not t2: continue
            t1 += 1; st1[t1] = st2[t2]; t2 -= 1
            s[t1] = s[t1 - 1] + st1[t1]
            f[t1] = max(f[t1 - 1], s[t1])
            continue
        else:
            k = int(c[1])
            print(f[k])
    
def main():
    s[0] = 0
    f[0] = -inf
    q = int(input())
    Editor(q)
    
main()