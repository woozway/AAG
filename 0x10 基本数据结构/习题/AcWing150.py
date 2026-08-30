import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    s = input_data[0]
    stk = []
    res = 0
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for i, c in enumerate(s):
        if stk and c in pairs and s[stk[-1]] == pairs[c]:
            stk.pop()
        else:
            stk.append(i)
            
        curr = i - stk[-1] if stk else i + 1
        if curr > res:
            res = curr
            
    print(res)

if __name__ == '__main__':
    main()