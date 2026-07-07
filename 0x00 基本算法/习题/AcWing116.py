import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    state = sum(
        1 << (i * 4 + j)
        for i in range(4) for j in range(4)
        if input_data[i][j] == '+'
    )
    
    masks = [
        sum(1 << (i * 4 + k) for k in range(4)) | sum(1 << (k * 4 + j) for k in range(4))
        for i in range(4) for j in range(4)
    ]
    
    best_path = None
    
    for i in range(65536):
        now = state
        for j in range(16):
            if (i >> j) & 1:
                now ^= masks[j]
                
        if now == 0:
            path = [(j // 4 + 1, j % 4 + 1) for j in range(16) if (i >> j) & 1]
            if best_path is None or len(path) < len(best_path):
                best_path = path
                
    if best_path is not None:
        print(len(best_path))
        for r, c in best_path:
            print(f"{r} {c}")

if __name__ == '__main__':
    main()