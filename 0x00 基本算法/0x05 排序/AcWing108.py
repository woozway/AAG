import sys

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
        
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    
    merged = []
    inv_count = inv_left + inv_right
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(int(x) for x in input_data)
    
    while True:
        try:
            n = next(iterator)
        except StopIteration:
            break
            
        grid_size = n * n
        
        a1 = [x for x in (next(iterator) for _ in range(grid_size)) if x != 0]
        _, res1 = count_inversions(a1)
        
        a2 = [x for x in (next(iterator) for _ in range(grid_size)) if x != 0]
        _, res2 = count_inversions(a2)
        
        if (res1 & 1) == (res2 & 1):
            print("TAK")
        else:
            print("NIE")

if __name__ == '__main__':
    main()