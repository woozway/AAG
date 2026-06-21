from math import sqrt

def calc(N, M):
    if N == 0: return (0, 0)
    len_, cnt = 1 << (N - 1), 1 << (2 * N - 2)
    x, y = calc(N - 1, M % cnt)
    z = M // cnt
    if z == 0: return (y, x)
    if z == 1: return (x, y + len_)
    if z == 2: return (x + len_, y + len_)
    if z == 3: return (2 * len_ - y - 1, len_ - x - 1)

def main():
    n = int(input())
    for _ in range(n):
        N, A, B = [int(x) for x in input().split()]
        ax, ay = calc(N, A - 1)
        bx, by = calc(N, B - 1)
        dx, dy = ax - bx, ay - by
        # python3中的四舍五入是银行家算法（舍入时向最近的偶数靠近）
        # print(round(sqrt(dx*dx + dy*dy) * 10))
        print(int(0.5 + sqrt(dx * dx + dy * dy) * 10))
        
main()