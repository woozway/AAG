import sys

class Node:
    def __init__(self, v):
        self.p = 0
        self.s = 1
        self.v = v
        self.avg = float(v)

def find(n, root, nodes):
    avg = 0.0
    res = -1
    for i in range(1, n + 1):
        if i != root and nodes[i].avg > avg:
            avg = nodes[i].avg
            res = i
    return res

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    root = int(input_data[1])
    
    nodes = [Node(0) for _ in range(n + 1)]
    ans = 0
    
    idx = 2
    for i in range(1, n + 1):
        v = int(input_data[idx])
        idx += 1
        nodes[i] = Node(v)
        ans += v
        
    for i in range(n - 1):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        nodes[b].p = a
        
    for i in range(n - 1):
        p = find(n, root, nodes)
        father = nodes[p].p
        
        ans += nodes[p].v * nodes[father].s
        nodes[p].avg = -1.0
        
        for j in range(1, n + 1):
            if nodes[j].p == p:
                nodes[j].p = father
                
        nodes[father].v += nodes[p].v
        nodes[father].s += nodes[p].s
        nodes[father].avg = nodes[father].v / nodes[father].s
        
    print(ans)

if __name__ == '__main__':
    main()