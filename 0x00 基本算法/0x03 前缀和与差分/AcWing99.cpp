#include <bits/stdc++.h>
using namespace std;
const int N = 5010;
int n, m;
int s[N][N];

int main() {
  int cnt, R;
  cin >> cnt >> R;
  R = min(5001, R); // 前缀和从1开始，横纵坐标 +1 后最大格子坐标 5001

  while (cnt -- ) {
    int x, y, w;
    cin >> x >> y >> w;
    x ++ , y ++ ; // 前缀和习惯从 1 开始，不用处理边界
    s[x][y] += w;
  }

  // 预处理二维前缀和：s[i][j] 表示 (1,1) 到 (i,j) 的矩形价值总和
  n = m = 5001;
  for (int i = 1; i <= n; i ++ )
    for (int j = 1; j <= m; j ++ )
      s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1];

  // 枚举边长为 R 的正方形的右下角坐标 (i, j)
  int res = 0;
  for (int i = R; i <= n; i ++ )
    for (int j = R; j <= m; j ++ )
      res = max(res, s[i][j] - s[i - R][j] - s[i][j - R] + s[i - R][j - R]);

  cout << res << endl;
  return 0;
}