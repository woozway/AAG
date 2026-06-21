#include <bits/stdc++.h>
using namespace std;
typedef pair<double, double> PDD;
const int N = 1010;
const double eps = 1e-6, INF = 1e10;
int n, d;
PDD seg[N];

// 将一个二维几何问题转化为了一维区间选点问题
int main() {
  cin >> n >> d;

  bool success = true;
  for (int i = 0; i < n; i ++ ) {
    int x, y;
    cin >> x >> y;
    if (y > d) {
      success = false;
      break;
    }
    auto len = sqrt(d * d - y * y); // 雷达须位于 [x - sqrt(d^2 - y^2), x + sqrt(d^2 - y^2)] 内
    seg[i] = {x + len, x - len}; // 存 <右端点, 左端点>，sort 时优先按 pair 的 first 从小到大排序
  }

  if (!success) puts("-1");
  else {
    sort(seg, seg + n);
    int res = 0;
    double last = -INF; // 记录上一个（最右边的一个）雷达建在 X 轴的哪个坐标
    for (int i = 0; i < n; i ++ )
      if (seg[i].second > last + eps) { // 说明上一个雷达覆盖不到当前小岛了
        res ++ ;
        last = seg[i].first; // 新建的雷达应建在“能覆盖当前小岛的范围内，最靠右的位置”
      }
    cout << res << endl;
  }
  return 0;
}