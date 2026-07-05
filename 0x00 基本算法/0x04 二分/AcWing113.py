# Forward declaration of compare API.
# def compare(a, b):
# @param a, b int
# @return bool
# return bool means whether a is less than b.

class Solution:
    def specialSort(self, n: int) -> list[int]:
        res = [1]
        for i in range(2, n + 1):
            l, r = 0, len(res) - 1
            while l < r:
                mid = (l + r + 1) >> 1
                if compare(res[mid], i):
                    l = mid
                else:
                    r = mid - 1
            
            res.append(i)
            for j in range(len(res) - 2, r, -1):
                res[j], res[j + 1] = res[j + 1], res[j]
            
            if not compare(res[r], i):
                res[r], res[r + 1] = res[r + 1], res[r]
                
        return res