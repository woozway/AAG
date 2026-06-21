// Forward declaration of compare API.
// bool compare(int a, int b);
// return bool means whether a is less than b.

class Solution {
public:
  vector<int> specialSort(int n) {
    vector<int> res;
    res.push_back(1);
    // 数学归纳法：假设前 i-1 个元素已排好，找到当前数组中“最后一个小于 i”的元素下标 r
    for (int i = 2; i <= n; i ++ ) {
      int l = 0, r = res.size() - 1;
      while (l < r) { // 分成：(..., x, x, x), (i, y, y, ...)
        int mid = l + r + 1 >> 1;
        if (compare(res[mid], i)) l = mid;
        else r = mid - 1;
      }
      res.push_back(i);
      // 挪位操作：将下标在 (r, 末尾) 之间的元素依次后移，给 i 腾出 r+1 的位置
      for (int j = res.size() - 2; j > r; j -- ) swap(res[j], res[j + 1]);
      // 边界特判：如果 res[r] 实际上大于 i（即 i 比当前所有数都小），则 i 需要换到最前面
      // if (r == 0 && !compare(res[0], i)) swap(res[0], res[1]);
      if (!compare(res[r], i)) swap(res[r], res[r + 1]);
    }
    return res;
  }
};