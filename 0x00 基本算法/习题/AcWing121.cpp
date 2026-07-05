#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;
const int N = 1010;
int n, C;
PII points[N];
int sum[N][N];
vector<int> numbers; // 用于离散化的数组，存储所有出现过的 X 和 Y 坐标

bool check(int len) { // 检查是否存在一个边长为 len 的正方形，能覆盖至少 C 个点
  // 双指针 x1 和 x2 代表我们要查询的 [真实的左右离散边界]
  for (int x1 = 1, x2 = 1; x2 < numbers.size(); x2 ++ ) {
    // 物理宽度 = 右边界的物理坐标 - 左边界的物理坐标 + 1，若超标，左边界 x1 必须向右收缩
    while (numbers[x2] - numbers[x1] + 1 > len) x1 ++ ;
    for (int y1 = 1, y2 = 1; y2 < numbers.size(); y2 ++ ) {
      while (numbers[y2] - numbers[y1] + 1 > len) y1 ++ ;
      if (sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1] >= C)
        return true;
    }
  }
  return false;
}

int find(int x) { // 二分查找实现 lower_bound：在去重后的 numbers 数组中找 x 的索引
  int l = 0, r = numbers.size() - 1;
  while (l < r) {
    int mid = l + r >> 1;
    if (numbers[mid] >= x) r = mid;
    else l = mid + 1;
  }
  return l;
}

int main() {
  cin >> C >> n;
  numbers.push_back(0); // 放入一个 0 作为哨兵，让二维前缀和的下标从 1 开始
  for (int i = 0; i < n; i ++ ) {
    int x, y;
    cin >> x >> y;
    numbers.push_back(x);
    numbers.push_back(y);
    points[i] = {x, y};
  }
  sort(numbers.begin(), numbers.end()); // 排序 + 去重
  numbers.erase(unique(numbers.begin(), numbers.end()), numbers.end());

  // 构建频数矩阵：把原始点映射到离散化后的网格中
  for (int i = 0; i < n; i ++ ) {
    int x = find(points[i].first), y = find(points[i].second);
    sum[x][y] ++ ;
  }
  // 二维前缀和：sum[i][j] 表示左上角 (1,1) 到右下角 (i,j) 这个矩形区域内的总点数
  for (int i = 1; i < numbers.size(); i ++ )
    for (int j = 1; j < numbers.size(); j ++ )
      sum[i][j] += sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];

  // 转二分判定：二分正方形的边长 len
  int l = 1, r = 10000;
  while (l < r) {
    int mid = l + r >> 1;
    if (check(mid)) r = mid;
    else l = mid + 1;
  }
  cout << l << endl;
  return 0;
}