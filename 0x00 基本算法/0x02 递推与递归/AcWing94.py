n, order, chosen = 0, [0] * 20, [0] * 20
def calc(k):
    if k == n + 1:
        for i in range(1, n + 1):
            print('%d ' % order[i], end='')
        print()
        return
    for i in range(1, n + 1):
        if chosen[i]: continue
        order[k] = i
        chosen[i] = 1
        calc(k + 1)
        chosen[i] = 0
        order[k] = 0

def main():
    global n
    n = int(input())
    calc(1)
    
main()