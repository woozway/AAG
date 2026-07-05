#include <bits/stdc++.h>
using namespace std;
const int N = 110;
int n;
int g[N][N];

int main() {
  cin >> n;
  for (int i = 1; i <= n; i ++ )
    for (int j = 1; j <= n; j ++ ) {
      cin >> g[i][j];
      g[i][j] += g[i - 1][j]; // 累加前缀和：g[i][j] 表示第 j 列从第 1 行到第 i 行的和
    }

  int res = INT_MIN;
  for (int i = 1; i <= n; i ++ ) // 枚举子矩阵的上边界 i 和下边界 j
    for (int j = i; j <= n; j ++ ) {
      int last = 0; // last：当前连续子段的和（一维最大子段和，Kadane 算法）
      for (int k = 1; k <= n; k ++ ) { // 枚举列，将二维的子矩阵压缩成一维数组来处理
        // g[j][k] - g[i - 1][k] 是当前第 k 列中，夹在上下边界 [i, j] 之间的元素和
        last = max(last, 0) + (g[j][k] - g[i - 1][k]);
        res = max(res, last);
      }
    }

  cout << res << endl;
  return 0;
}