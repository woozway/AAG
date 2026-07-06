def main():
    d = [2**i - 1 for i in range(13)]
    f = [0] * 13
    
    for i in range(1, 13):
        f[i] = min(2 * f[j] + d[i - j] for j in range(i))
        print(f[i])

if __name__ == '__main__':
    main()