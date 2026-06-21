N = 26
n, num, top, t = 0, 0, 0, 0
st, ans = [0] * N, [0] * N

def z(x):
    global n, num, top, t
    if x == n + 1:
        num += 1
        if num > 20: exit(0)
        for i in range(1, t + 1): print(ans[i], end='')
        for i in range(top, 0, -1): print(st[i], end='')
        print()
        return
    if top:
        t += 1; ans[t] = st[top]; top -= 1
        z(x)
        top += 1; st[top] = ans[t]; t -= 1
    top += 1; st[top] = x
    z(x + 1)
    top -= 1

def main():
    global n
    n = int(input())
    z(1)
    
main()