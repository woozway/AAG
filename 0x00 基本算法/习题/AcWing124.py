import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    try:
        T = int(next(iterator))
    except StopIteration:
        return
        
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    char_map = {c: i for i, c in enumerate(chars)}
    
    for _ in range(T):
        a = int(next(iterator))
        b = int(next(iterator))
        a_line = next(iterator)
        
        val = 0
        for char in a_line:
            val = val * a + char_map[char]
            
        if val == 0:
            b_line = "0"
        else:
            res = []
            while val > 0:
                res.append(chars[val % b])
                val //= b
            b_line = "".join(reversed(res))
            
        print(f"{a} {a_line}")
        print(f"{b} {b_line}")
        print()

if __name__ == '__main__':
    main()