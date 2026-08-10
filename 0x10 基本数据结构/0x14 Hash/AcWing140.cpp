#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ULL;
const int N = 3e5 + 10, base = 131;
int n;
char str[N];
ULL h[N], p[N];
int sa[N]; // Suffix Array (后缀数组)，sa[i] 表示排名为 i 的后缀的起始下标

ULL get(int l, int r) {
  return h[r] - h[l - 1] * p[r - l + 1];
}

// 获取以 a 和 b 为起始下标的两个后缀的最长公共前缀 (LCP) 的长度
int get_max_common_prefix(int a, int b) {
  int l = 0, r = min(n - a + 1, n - b + 1); // 半径不超过两个后缀各自的长度
  while (l < r) {
    int mid = l + r + 1 >> 1;
    if (get(a, a + mid - 1) != get(b, b + mid - 1)) r = mid - 1;
    else l = mid;
  }
  return l;
}

// 用于比较后缀 a 和后缀 b 的字典序
bool cmp(int a, int b) {
  int l = get_max_common_prefix(a, b);
  // 若 a + l > n，说明后缀 a 是 b 的前缀（即后缀 a 已结束）
  int av = a + l > n ? INT_MIN : str[a + l];
  int bv = b + l > n ? INT_MIN : str[b + l];
  return av < bv;
}

int main() {
  scanf("%s", str + 1);
  n = strlen(str + 1);

  p[0] = 1;
  for (int i = 1; i <= n; i ++ ) {
    h[i] = h[i - 1] * base + str[i] - 'a' + 1;
    p[i] = p[i - 1] * base;
    sa[i] = i;
  }

  sort(sa + 1, sa + 1 + n, cmp); // O(N log^2 N)

  // 计算并输出排名相邻的两个后缀的最长公共前缀 LCP
  for (int i = 1; i <= n; i ++ ) printf("%d ", sa[i] - 1);
  puts("");
  for (int i = 1; i <= n; i ++ )
    if (i == 1) printf("0 "); // 排名第一的后缀没有前驱，LCP 规定为 0
    else printf("%d ", get_max_common_prefix(sa[i - 1], sa[i]));
  puts("");

  return 0;
}