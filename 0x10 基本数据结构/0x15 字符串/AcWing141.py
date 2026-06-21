a, nxt = [0] * 1000010, [0] * 1000010
n, T = 0, 0

def calc_next():
    global n, T
    nxt[1], j = 0, 0
    for i in range(2, n + 1):
        while j > 0 and a[i] != a[j + 1]: j = nxt[j]
        if a[i] == a[j + 1]: j += 1
        nxt[i] = j

def main():
    global n, T
    while True:
        n = int(input())
        if n == 0: break
        a[1:] = list(input())
        calc_next()
        T += 1; print("Test case #%d" %T)
        for i in range(2, n + 1):
            if i % (i - nxt[i]) == 0 and i // (i - nxt[i]) > 1:
                print("%d %d" %(i, i // (i - nxt[i])))
        print()
        
main()