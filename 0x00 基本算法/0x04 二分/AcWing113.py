# Forward declaration of compare API.
# def compare(a, b):
# @param a, b int
# @return bool
# return bool means whether a is less than b.

class Solution(object):
    def specialSort(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        a = []
        for i in range(N): a.append(i + 1)
        for i in range(N):
            k = a[i]
            l, r = 0, k - 1
            while l < r:
                mid = (l + r) >> 1
                if compare(k, a[mid]): r = mid
                else: l = mid + 1
            for j in range(i - 1, l - 1, -1): a[j + 1] = a[j]
            a[l] = k
        return a