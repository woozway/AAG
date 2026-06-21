#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<LL, LL> PLL;

// 顺时针旋转 theta = 90 deg（向量右乘旋转矩阵）再水平翻转（theta = 270 同理）
// Rotation matrix: | cosθ, -sinθ |
//                  | sinθ,  cosθ |

// calc(N, M) 返回编号为 M 的房屋（从0开始）在 N 级城市中的位置
// len 表示组成 N 级城市的所有 N-1 级正方形边长（一个格子记为 1，尚未乘 10）
// cnt 表示组成 N 级城市的所有 N-1 级城市的个数：4^(n-1)
PLL calc(LL n, LL m) {
  if (!n) return {0, 0};
  // 这里因为 N<=31，2*N-2 会超出 int 表示范围，所以加 ll
  LL len = 1ll << n - 1, cnt = 1ll << 2 * (n - 1);
  auto pos = calc(n - 1, m % cnt);
  auto x = pos.first, y = pos.second;
  auto z = m / cnt;
  if (z == 0) return {y, x}; // 左上格子，(x,y) -> (-y,x) -> (y,x)
  if (z == 1) return {x, y + len}; // 右上
  if (z == 2) return {x + len, y + len}; // 右下
  return {-y + len * 2 - 1, -x + len - 1}; // 左下，(x,y) -> (y,-x) -> (-y,-x)
}

int main() {
  int T;
  cin >> T;
  while (T -- ) {
    LL N, A, B;
    cin >> N >> A >> B;
    auto ac = calc(N, A - 1);
    auto bc = calc(N, B - 1);
    double x = ac.first - bc.first, y = ac.second - bc.second;
    // cout << (LL)round(sqrt(x * x + y * y) * 10) << endl;
    printf("%.0lf\n", sqrt(x * x + y * y) * 10);
  }
  return 0;
}