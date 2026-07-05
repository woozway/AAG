import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    def dfs(u, sum_val, state):
        if sum_val + n - u < m:
            return
        if sum_val == m:
            for i in range(n):
                if (state >> i) & 1:
                    print(i + 1, end=' ')
            print()
            return

        dfs(u + 1, sum_val + 1, state + (1 << u))
        dfs(u + 1, sum_val, state)

    dfs(0, 0, 0)

if __name__ == '__main__':
    main()