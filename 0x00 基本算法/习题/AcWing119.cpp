#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10, INF = 1e10;
struct Point {
  double x, y;
  bool type; // 标记点属于集合 A(0) 还是集合 B(1)
  bool operator< (const Point &W) const {
    return x < W.x;
  }
} points[N], temp[N];

double dist(Point &a, Point &b) {
  if (a.type == b.type) return INF;
  double dx = a.x - b.x, dy = a.y - b.y;
  return sqrt(dx * dx + dy * dy);
}

double dfs(int l, int r) { // 分治法核心函数：在区间 [l, r] 内找不同集合的最短距离
  if (l >= r) return INF;

  int mid = l + r >> 1;
  double mid_x = points[mid].x;
  // 递归求出左半部分的最小距离，和右半部分的最小距离，取两者中的较小值 res
  double res = min(dfs(l, mid), dfs(mid + 1, r));
  // Y 坐标归并排序，用双指针 i 和 j，将这两个有序序列合并成一个按 Y 坐标排序的大序列
  {
    int k = 0, i = l, j = mid + 1;
    while (i <= mid && j <= r)
      if (points[i].y < points[j].y) temp[k ++ ] = points[i ++ ];
      else temp[k ++ ] = points[j ++ ];
    while (i <= mid) temp[k ++ ] = points[i ++ ];
    while (j <= r) temp[k ++ ] = points[j ++ ];
    for (i = 0, j = l; i < k; i ++ , j ++ ) points[j] = temp[i];
  }
  // 处理跨越中轴线的点对：只有 X 坐标距离中轴线在 res 范围内的点，
  // 才有可能构成更短的距离，将可能的“候选点”筛选到 temp 数组中
  int k = 0;
  for (int i = l; i <= r; i ++ )
    if (points[i].x >= mid_x - res && points[i].x <= mid_x + res)
      temp[k ++ ] = points[i];

  // 由于 temp 数组已按 Y 坐标排好序，第二个for循环中最多只往回找 6~7 个点，O(1)
  for (int i = 0; i < k; i ++ )
    for (int j = i - 1; j >= 0 && temp[i].y - temp[j].y < res; j -- )
      res = min(res, dist(temp[i], temp[j]));

  return res;
}

int main() {
  int T, n;
  cin >> T;

  while (T -- ) {
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ) {
      scanf("%lf%lf", &points[i].x, &points[i].y);
      points[i].type = 0;
    }
    for (int i = n; i < 2 * n; i ++ ) {
      scanf("%lf%lf", &points[i].x, &points[i].y);
      points[i].type = 1;
    }
    // 例如所有点都在同一条直线上，打乱顺序可以有效防止快速排序 / 分治退化
    random_shuffle(points, points + n * 2);
    // 首次全局排序：按照 X 坐标从小到大排序，为后续的按 X 坐标分治做准备
    sort(points, points + n * 2);
    printf("%.3lf\n", dfs(0, n * 2 - 1));
  }

  return 0;
}