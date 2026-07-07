import sys

def main():
    fractals = [['X']]
    for _ in range(6):
        prev = fractals[-1]
        empty = ' ' * len(prev)
        curr = [r + empty + r for r in prev] + \
               [empty + r + empty for r in prev] + \
               [r + empty + r for r in prev]
        fractals.append(curr)

    input_data = sys.stdin.read().split()
    for token in input_data:
        n = int(token)
        if n == -1:
            break
        print('\n'.join(fractals[n - 1]))
        print('-')

if __name__ == '__main__':
    main()