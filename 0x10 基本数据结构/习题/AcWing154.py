import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:n + 2]]

    min_res = []
    q = deque()
    for i in range(n):
        if q and q[0] < i - k + 1:
            q.popleft()
        while q and a[q[-1]] >= a[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            min_res.append(str(a[q[0]]))

    max_res = []
    q.clear()
    for i in range(n):
        if q and q[0] < i - k + 1:
            q.popleft()
        while q and a[q[-1]] <= a[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            max_res.append(str(a[q[0]]))

    sys.stdout.write(' '.join(min_res) + '\n')
    sys.stdout.write(' '.join(max_res) + '\n')

if __name__ == '__main__':
    main()