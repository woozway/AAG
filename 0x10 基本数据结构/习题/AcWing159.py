import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    strings = input_data[2:n + 2]
    
    width = m
    for j in range(1, m + 1):
        if all(s[j:] == s[:-j] for s in strings):
            width = j
            break
            
    truncated = [s[:width] for s in strings]
    
    ne = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and truncated[i] != truncated[j]:
            j = ne[j - 1]
        if truncated[i] == truncated[j]:
            j += 1
        ne[i] = j
        
    height = n - ne[-1]
    
    print(width * height)

if __name__ == '__main__':
    main()