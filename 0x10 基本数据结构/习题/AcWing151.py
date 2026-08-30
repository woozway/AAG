import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    s = input_data[0]
    
    if s and s[0] == '-':
        s = '0' + s
        
    s = '(' * (len(s) + 1) + s + ')'
    
    nums = []
    ops = []
    
    def cal():
        a = nums.pop()
        b = nums.pop()
        c = ops.pop()
        
        if c == '+':
            nums.append(b + a)
        elif c == '-':
            nums.append(b - a)
        elif c == '*':
            nums.append(b * a)
        elif c == '/':
            nums.append(int(b / a))
        elif c == '^':
            nums.append(b ** a)

    i = 0
    n = len(s)
    
    while i < n:
        if s[i].isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1
            nums.append(int(s[i:j]))
            i = j - 1
        else:
            c = s[i]
            if c == '(':
                ops.append(c)
            elif c in '+-':
                if c == '-' and i > 0 and not s[i - 1].isdigit() and s[i - 1] != ')':
                    if i + 1 < n and s[i + 1] == '(':
                        nums.append(-1)
                        ops.append('*')
                    else:
                        j = i + 1
                        while j < n and s[j].isdigit():
                            j += 1
                        nums.append(-int(s[i + 1:j]))
                        i = j - 1
                else:
                    while ops and ops[-1] != '(':
                        cal()
                    ops.append(c)
            elif c in '*/':
                while ops and ops[-1] in '*/^':
                    cal()
                ops.append(c)
            elif c == '^':
                while ops and ops[-1] == '^':
                    cal()
                ops.append(c)
            elif c == ')':
                while ops and ops[-1] != '(':
                    cal()
                if ops:
                    ops.pop()
        i += 1

    while ops:
        if ops[-1] == '(':
            ops.pop()
        else:
            cal()

    if nums:
        print(nums[0])

if __name__ == '__main__':
    main()