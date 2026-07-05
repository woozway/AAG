import sys

n = 0
path = []

def dfs(u, state):
    if u == n:
        print(*(path))
        return

    for i in range(n):
        if not ((state >> i) & 1):
            path.append(i + 1)
            dfs(u + 1, state + (1 << i))
            path.pop()

def main():
    global n
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    dfs(0, 0)

if __name__ == '__main__':
    main()