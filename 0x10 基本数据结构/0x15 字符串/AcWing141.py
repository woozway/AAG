import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = iter(input_data)
    T = 1
    
    for n_str in it:
        n = int(n_str)
        if n == 0:
            break
            
        s = next(it)
        
        nxt = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
            
        sys.stdout.write(f"Test case #{T}\n")
        T += 1
        
        for i in range(1, n):
            length = i + 1
            t = length - nxt[i]
            if length > t and length % t == 0:
                sys.stdout.write(f"{length} {length // t}\n")
        sys.stdout.write("\n")

if __name__ == '__main__':
    main()