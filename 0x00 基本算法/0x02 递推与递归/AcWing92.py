n, chosen = 0, []
def calc(x):
    if x == n + 1:
        for i in range(len(chosen)):
            print("%d " % chosen[i], end='')
        print()
        return
    calc(x + 1)
    chosen.append(x)
    calc(x + 1)
    chosen.pop()

def main():
    global n
    n = int(input())
    calc(1)
    
main()