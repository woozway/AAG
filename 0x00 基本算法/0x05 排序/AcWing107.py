import sys

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
        if n == 0:
            break
            
        a = [next(iterator) for _ in range(n)]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
                
            mid = len(arr) // 2
            left, left_inv = merge_sort(arr[:mid])
            right, right_inv = merge_sort(arr[mid:])
            
            merged = []
            inv_count = left_inv + right_inv
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

        _, total_inv = merge_sort(a)
        print(total_inv)

if __name__ == '__main__':
    main()