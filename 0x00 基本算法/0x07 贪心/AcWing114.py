import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    try:
        n = next(iterator)
        ka = next(iterator)
        kb = next(iterator)
    except StopIteration:
        return
        
    ministers = []
    for _ in range(n):
        ministers.append((next(iterator), next(iterator)))
        
    ministers.sort(key=lambda x: x[0] * x[1])
    
    max_reward = 0
    current_product = ka
    
    for a, b in ministers:
        reward = current_product // b
        if reward > max_reward:
            max_reward = reward
        current_product *= a
        
    print(max_reward)

if __name__ == '__main__':
    main()