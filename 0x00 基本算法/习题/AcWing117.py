import sys

def main():
    closed = [[] for _ in range(14)]
    open_count = [0] * 14
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    for i in range(1, 14):
        for j in range(4):
            s = input_data[idx]
            idx += 1
            if '2' <= s[0] <= '9':
                x = int(s[0])
            elif s[0] == '0':
                x = 10
            elif s[0] == 'A':
                x = 1
            elif s[0] == 'J':
                x = 11
            elif s[0] == 'Q':
                x = 12
            else:
                x = 13
            closed[i].append(x)
            
    for i in range(4):
        t = closed[13][i]
        while t != 13:
            open_count[t] += 1
            r = t
            t = closed[r].pop()
            
    res = 0
    for i in range(1, 13):
        if open_count[i] >= 4:
            res += 1
            
    print(res)

if __name__ == '__main__':
    main()