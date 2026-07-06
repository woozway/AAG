import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    T = int(input_data[0])
    idx = 1
    
    dx = (0, -1, 0, 1, 0)
    dy = (0, 0, 1, 0, -1)
    
    for _ in range(T):
        g = [[int(c) for c in input_data[idx + i]] for i in range(5)]
        idx += 5
        
        ans = float('inf')
        
        for k in range(32):
            res = 0
            curr = [row[:] for row in g]
            
            def turn(x, y):
                for d in range(5):
                    a, b = x + dx[d], y + dy[d]
                    if 0 <= a < 5 and 0 <= b < 5:
                        curr[a][b] ^= 1

            for j in range(5):
                if (k >> j) & 1:
                    res += 1
                    turn(0, j)
                    
            for i in range(4):
                for j in range(5):
                    if curr[i][j] == 0:
                        res += 1
                        turn(i + 1, j)
                        
            if sum(curr[4]) == 5:
                if res < ans:
                    ans = res
                    
        print(ans if ans <= 6 else -1)

if __name__ == '__main__':
    main()