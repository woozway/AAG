stk, top, address = [0] * 100010, 0, 0
chosen = []
def calc(x, ret_addr):
    global top, stk
    old_top = top
    top += 1; stk[top] = x
    top += 1; stk[top] = ret_addr
    top += 1; stk[top] = old_top

def ret():
    global top, stk
    ret_addr = stk[top - 1]
    top = stk[top]
    return ret_addr
    
def main():
    global stk, top, address
    n, m = [int(x) for x in input().split()]
    calc(1, 0)
    while top:
        x = stk[top - 2]
        if address == 0:
            if len(chosen) > m or len(chosen) + (n - x + 1) < m:
                address = ret()
                continue
            if x == n + 1:
                for i in range(len(chosen)):
                    print("%d " %chosen[i], end='')
                print()
                address = ret()
                continue
            chosen.append(x)
            calc(x + 1, 1)
            address = 0
            continue
        elif address == 1:
            chosen.pop()
            calc(x + 1, 2)
            address = 0
            continue
        else:
            address = ret()
            
main()