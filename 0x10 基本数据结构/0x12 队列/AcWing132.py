import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    scenario = 1
    
    while True:
        try:
            n = int(next(iterator))
        except StopIteration:
            break
            
        if n == 0:
            break
            
        print(f"Scenario #{scenario}")
        scenario += 1
        
        team_id = {}
        for i in range(n):
            cnt = int(next(iterator))
            for _ in range(cnt):
                team_id[next(iterator)] = i
                
        team_queue = deque()
        person_queues = [deque() for _ in range(n)]
        
        while True:
            cmd = next(iterator)
            if cmd == "STOP":
                break
            elif cmd == "ENQUEUE":
                x = next(iterator)
                tid = team_id[x]
                if not person_queues[tid]:
                    team_queue.append(tid)
                person_queues[tid].append(x)
            else:
                tid = team_queue[0]
                print(person_queues[tid].popleft())
                if not person_queues[tid]:
                    team_queue.popleft()
                    
        print()

if __name__ == '__main__':
    main()