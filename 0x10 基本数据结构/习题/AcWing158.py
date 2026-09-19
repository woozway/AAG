import sys

def get_min(s, n):
    i = 0
    j = 1
    while i < n and j < n:
        k = 0
        while k < n and s[i + k] == s[j + k]:
            k += 1
        if k == n:
            break
        if s[i + k] > s[j + k]:
            i += k + 1
        else:
            j += k + 1
        if i == j:
            i += 1
    return min(i, j)

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
        
    a = input_data[0]
    b = input_data[1]
    
    n = len(a)
    
    a2 = a * 2
    b2 = b * 2
    
    ia = get_min(a2, n)
    ib = get_min(b2, n)
    
    min_a = a2[ia:ia + n]
    min_b = b2[ib:ib + n]
    
    if min_a == min_b:
        print("Yes")
        print(min_a)
    else:
        print("No")

if __name__ == '__main__':
    main()