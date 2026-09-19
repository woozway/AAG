#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ULL;
const int N = 1010, M = N * N, P = 131;
int n, m, a, b;
ULL hashv[N][N], p[M]; // hashv[i][j]: 第 i 行前 j 个字符构成的前缀哈希值
char str[N];

// 计算第 f 行中，区间 [l, r] 这个子串的 1D 哈希值
ULL get(ULL f[], int l, int r) {
  return f[r] - f[l - 1] * p[r - l + 1];
}

int main() {
  scanf("%d%d%d%d", &n, &m, &a, &b);

  p[0] = 1;
  for (int i = 1; i <= n * m; i ++ ) p[i] = p[i - 1] * P;

  for (int i = 1; i <= n; i ++ ) { // 预处理大矩阵每一行的 1D 前缀哈希值
    scanf("%s", str + 1);
    for (int j = 1; j <= m; j ++ ) hashv[i][j] = hashv[i][j - 1] * P + str[j] - '0';
  }

  unordered_set<ULL> S; // 滑动窗口计算所有 a * b 尺寸子矩阵的 2D 哈希值，并存入哈希表 S
  for (int i = b; i <= m; i ++ ) { // 子矩阵的右边界列 i，保证宽度恒定为 b
    ULL s = 0;
    int l = i - b + 1, r = i;
    for (int j = 1; j <= n; j ++ ) { // 滑动窗口在固定的列区间内，从上到下按行滑动
      s = s * p[b] + get(hashv[j], l, r); // 加上新进入窗口的第 j 行区间 [l, r] 的哈希值
      if (j - a > 0) s -= get(hashv[j - a], l, r) * p[a * b]; // 减去滑出窗口的那一行
      if (j >= a) S.insert(s); // 将一个完整的 a * b 子矩阵的 2D 哈希值加入集合 S
    }
  }

  int k;
  scanf("%d", &k);
  while (k -- ) {
    ULL s = 0;
    for (int i = 0; i < a; i ++ ) {
      scanf("%s", str);
      for (int j = 0; j < b; j ++ ) s = s * P + str[j] - '0';
    }
    if (S.count(s)) puts("1");
    else puts("0");
  }

  return 0;
}