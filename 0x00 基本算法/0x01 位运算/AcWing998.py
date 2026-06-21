n, m, a = 0, 0, [[None] * 2 for i in range(100005)]
def calc(bit, now):
    for i in range(1, n + 1):
        x = a[i][1] >> bit & 1
        if a[i][0] == "AND": now &= x
        elif a[i][0] == "OR": now |= x
        else: now ^= x
    return now
    
def main():
    global n, m, a
    n, m = [int(x) for x in input().split()]
    for i in range(1, n + 1):
        s, x = input().split()
        a[i] = [s, int(x)]
        
    val, ans = 0, 0
    for bit in range(29, -1, -1):
        res0 = calc(bit, 0)
        res1 = calc(bit, 1)
        if val + (1 << bit) <= m and res0 < res1:
            val += 1 << bit; ans += 1 << bit
        else:
            ans += res0 << bit
    print(ans)

main()