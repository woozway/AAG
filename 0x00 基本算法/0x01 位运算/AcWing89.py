import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return
    
    a = int(input_data[0])
    b = int(input_data[1])
    p = int(input_data[2])

    res = 1 % p
    while b > 0:
        if b & 1:
            res = (res * a) % p
        a = (a * a) % p
        b >>= 1

    print(res)

if __name__ == '__main__':
    main()