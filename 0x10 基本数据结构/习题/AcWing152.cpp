#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
int n, m;
char g[N][N];
int h[N][N]; // h[i][j] 表示第 i 行第 j 列，向上连续 'F' 的个数（即直方图的高度）
// l[i]: 存储第 i 根柱子向左延伸时，高度大于等于 a[i] 的最左侧列下标
// r[i]: 临时存储数组翻转后，翻转数组中每根柱子向左延伸的最左侧列下标
int q[N], l[N], r[N];

// 单调栈求左边界，a: 当前行的直方图高度数组，l: 用于存储计算出的左边界数组
void get(int a[], int l[]) {
  int tt = 0;
  q[0] = 0;
  a[0] = -1; // 哨兵：下标 0 处放置极小值 -1，保证栈底永远不会被弹出，省去判空的麻烦
  for (int i = 1; i <= m; i ++ ) {
    while (a[q[tt]] >= a[i]) tt -- ;
    l[i] = q[tt] + 1;
    q[ ++ tt] = i;
  }
}

// 计算当前行直方图构成的最大矩形面积
int work(int a[]) {
  get(a, l); // 求出每个柱子作为矩形高度时，向左能延伸到的最远下标 l[i]
  reverse(a + 1, a + 1 + m);
  get(a, r); // 这里直接将数组翻转，翻转后的“向左延伸左边界”，就完全等价于原数组的“向右延伸右边界”
  reverse(a + 1, a + 1 + m);

  // i 翻转后对应的下标是 (m + 1 - i)，r[m + 1 - i] 是它在翻转数组中的最左有效位置
  // 再用 m + 1 减去它，就能映射回原数组中的最右有效位置 right
  int res = 0;
  for (int i = 1; i <= m; i ++ ) {
    int left = l[i];
    int right = (m + 1) - r[m + 1 - i];
    res = max(res, a[i] * (right - left + 1));
  }
  return res;
}

int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; i ++ )
    for (int j = 1; j <= m; j ++ ) {
      cin >> g[i][j];
      if (g[i][j] == 'F') h[i][j] = h[i - 1][j] + 1;
      else h[i][j] = 0;
    }

  int res = 0;
  for (int i = 1; i <= n; i ++ ) res = max(res, work(h[i]));
  cout << res * 3 << endl;
  return 0;
}