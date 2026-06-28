#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
char g[N][N];

void dfs(int n) {
  if (n == 1) {
    g[0][0] = 'X';
    return;
  }
  // 递归调用：先在画布左上角画出规模为 n-1 的图形
  dfs(n - 1); // 此时左上角图案已生成好，只需把它“复制粘贴”到另外 4 个位置

  int len = 1; // 计算上一级图形的边长 len：规模为 1 边长是 1，规模 2 边长 3...
  for (int i = 0; i < n - 2; i ++ ) len *= 3;

  // 将 n 级图形均分为 3x3 的九宫格，上一级图形需要被复制到其中 4 个区块
  // 这 4 个区块在九宫格中的逻辑坐标 (行号, 列号) 分别是：(0,2), (1,1), (2,0), (2,2)
  int sx[4] = {0, 1, 2, 2}, sy[4] = {2, 1, 0, 2};
  for (int k = 0; k < 4; k ++ )
    for (int i = 0; i < len; i ++ )
      for (int j = 0; j < len; j ++ )
        g[sx[k] * len + i][sy[k] * len + j] = g[i][j];
}

int main() {
  dfs(7); // 直接在程序一开始，就把 n=7 的终极图形画在画布上
          // 后续只要查询小的 n，只需要截取画布左上角的一部分输出即可
  int n;
  while (cin >> n, n != -1) {
    int k = 1;
    while ( -- n) k *= 3; // 计算当前要查询的图形边长 k = 3^(n-1)

    for (int i = 0; i < k; i ++ ) {
      for (int j = 0; j < k; j ++ )
        if (g[i][j]) cout << g[i][j];
        else cout << ' ';
      cout << endl;
    }
    cout << '-' << endl;
  }
  return 0;
}