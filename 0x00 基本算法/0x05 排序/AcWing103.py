import sys
from collections import Counter

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    n = next(iterator)
    counts = Counter(next(iterator) for _ in range(n))
    
    m = next(iterator)
    b = [next(iterator) for _ in range(m)]
    c = [next(iterator) for _ in range(m)]
    
    best_movie = 1
    max_audio = -1
    max_sub = -1
    
    for i in range(m):
        audio, sub = counts[b[i]], counts[c[i]]
        if (audio, sub) > (max_audio, max_sub):
            max_audio, max_sub = audio, sub
            best_movie = i + 1
            
    print(best_movie)

if __name__ == '__main__':
    main()