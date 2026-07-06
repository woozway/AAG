import sys

class Node:
    __slots__ = ['p', 's', 'v', 'avg']
    
    def __init__(self, v):
        self.p = 0
        self.s = 1
        self.v = v
        self.avg = float(v)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    try:
        n = next(iterator)
        root = next(iterator)
    except StopIteration:
        return
        
    nodes = [None]
    ans = 0
    
    for _ in range(n):
        v = next(iterator)
        nodes.append(Node(v))
        ans += v
        
    for _ in range(n - 1):
        a = next(iterator)
        b = next(iterator)
        nodes[b].p = a
        
    for _ in range(n - 1):
        max_avg = -1.0
        p = -1
        
        for i in range(1, n + 1):
            if i != root and nodes[i].avg > max_avg:
                max_avg = nodes[i].avg
                p = i
                
        father = nodes[p].p
        ans += nodes[p].v * nodes[father].s
        nodes[p].avg = -1.0
        
        for i in range(1, n + 1):
            if nodes[i].p == p:
                nodes[i].p = father
                
        nodes[father].v += nodes[p].v
        nodes[father].s += nodes[p].s
        nodes[father].avg = nodes[father].v / nodes[father].s
        
    print(ans)

if __name__ == '__main__':
    main()