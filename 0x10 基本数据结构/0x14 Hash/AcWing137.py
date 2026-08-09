import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    idx = 1
    seen = set()
    
    for _ in range(n):
        s = tuple(int(x) for x in input_data[idx:idx+6])
        idx += 6
        
        rs = s[::-1]
        canonical = min(
            [s[i:] + s[:i] for i in range(6)] + 
            [rs[i:] + rs[:i] for i in range(6)]
        )
        
        if canonical in seen:
            print("Twin snowflakes found.")
            return
        seen.add(canonical)
        
    print("No two snowflakes are alike.")

if __name__ == '__main__':
    main()