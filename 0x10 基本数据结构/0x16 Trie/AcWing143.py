import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    nums = [int(x) for x in input_data[1:]]
    trie = [[0, 0]]
    
    max_xor = 0
    for x in nums:
        p = 0
        for i in range(30, -1, -1):
            bit = (x >> i) & 1
            if not trie[p][bit]:
                trie.append([0, 0])
                trie[p][bit] = len(trie) - 1
            p = trie[p][bit]
            
        p = 0
        curr_xor = 0
        for i in range(30, -1, -1):
            bit = (x >> i) & 1
            inv_bit = bit ^ 1
            if trie[p][inv_bit]:
                curr_xor |= (1 << i)
                p = trie[p][inv_bit]
            else:
                p = trie[p][bit]
                
        if curr_xor > max_xor:
            max_xor = curr_xor
            
    print(max_xor)

if __name__ == '__main__':
    main()