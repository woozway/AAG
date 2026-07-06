import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    p = [(input_data[i], int(input_data[i + 1])) for i in range(2, 2 + n * 2, 2)]
        
    def calc(bit, now):
        for op, x in p:
            b = (x >> bit) & 1
            if op == "AND":
                now &= b
            elif op == "OR":
                now |= b
            else:
                now ^= b
        return now

    t = res = 0
    for i in range(30, -1, -1):
        a, b = calc(i, 0), calc(i, 1)
        if t + (1 << i) <= m and a < b:
            t += 1 << i
            res += b << i
        else:
            res += a << i
            
    print(res)

if __name__ == '__main__':
    main()