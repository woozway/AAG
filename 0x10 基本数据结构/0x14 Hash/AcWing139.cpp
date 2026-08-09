#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ULL;
const int N = 2e6 + 10, base = 131; // 2 倍长度
char str[N];
ULL hl[N], hr[N], p[N]; // hl: 正向前缀哈希; hr: 把原字符串翻转后的前缀哈希

ULL get(ULL h[], int l, int r) {
  return h[r] - h[l - 1] * p[r - l + 1];
}

int main() {
  int T = 1;
  while (scanf("%s", str + 1), strcmp(str + 1, "END")) {
    int n = strlen(str + 1);
    for (int i = n * 2; i; i -= 2) { // 插入特殊字符，统一奇偶回文串
      str[i] = str[i / 2];
      str[i - 1] = 'a' + 26;
    }
    n *= 2; // 长度变化 2 倍

    p[0] = 1; // 预处理正向和反向的哈希前缀数组
    for (int i = 1, j = n; i <= n; i ++ , j -- ) {
      hl[i] = hl[i - 1] * base + str[i] - 'a' + 1; 
      hr[i] = hr[i - 1] * base + str[j] - 'a' + 1;
      p[i] = p[i - 1] * base;
    }

    int res = 0; // 枚举每个点作为回文中心，二分查找最大回文半径
    for (int i = 1; i <= n; i ++ ) {
      int l = 0, r = min(i - 1, n - i); // 半径最大不能超过中心点到左右边界的距离
      while (l < r) {
        int mid = l + r + 1 >> 1;
        // 左半：[i - mid, i - 1]；右半：[i + 1, i + mid]
        // 原串中下标为 k 的字符，在翻转后的字串中，其下标变成了 (n+1 - k)
        if (get(hl, i - mid, i - 1) != get(hr, n + 1 - (i + mid), n + 1 - (i + 1)))
          r = mid - 1;
        else
          l = mid;
      }
      // 如果最左边是一个真实的字母（<= 'z'），则真实字母的数量正好是半径 l + 1
      if (str[i - l] <= 'z') res = max(res, l + 1);
      else res = max(res, l);
    }

    printf("Case %d: %d\n", T ++ , res);
  }

  return 0;
}