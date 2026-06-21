from collections import deque

N, T = 1000000, 1006
t, f, _id, q = 0, [0] * N, 0, [0] * T

def Team_Queue():
    global t, f, _id, q
    q[0] = deque()
    for i in range(1, t + 1):
        _, *rest = [int(x) for x in input().split()]
        for x in rest: f[x] = i
        q[i] = deque()
    _id += 1
    print("Scenario #%d" %_id)
    while True:
        s, *rest = input().split()
        if s[0] == 'S': break
        if s[0] == 'E':
            x = int(rest[0])
            if not q[f[x]]: q[0].append(f[x])
            q[f[x]].append(x)
        else:
            x = q[0][0]
            print(q[x].popleft())
            if not q[x]: q[0].popleft()
    print()
    
def main():
    global t, f, _id, q
    while True:
        t = int(input())
        if t == 0: break
        Team_Queue()
        
main()