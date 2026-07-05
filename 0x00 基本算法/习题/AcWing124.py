import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    for _ in range(T):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        a_line = input_data[idx + 2]
        idx += 3
        
        number = []
        for c in a_line:
            if '0' <= c <= '9':
                number.append(ord(c) - ord('0'))
            elif 'A' <= c <= 'Z':
                number.append(ord(c) - ord('A') + 10)
            else:
                number.append(ord(c) - ord('a') + 36)
        
        number.reverse()
        
        res = []
        while number:
            t = 0
            for i in range(len(number) - 1, -1, -1):
                number[i] += t * a
                t = number[i] % b
                number[i] //= b
            res.append(t)
            while number and number[-1] == 0:
                number.pop()
        
        res.reverse()
        b_line = ""
        for x in res:
            if x <= 9:
                b_line += chr(ord('0') + x)
            elif x <= 35:
                b_line += chr(ord('A') + x - 10)
            else:
                b_line += chr(ord('a') + x - 36)
        
        print(f"{a} {a_line}")
        print(f"{b} {b_line}")
        print()

if __name__ == '__main__':
    main()