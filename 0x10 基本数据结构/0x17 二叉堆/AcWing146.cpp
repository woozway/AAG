#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII; // <当前组合的和s, 这个和在数组 a 中对应的下标p>
const int N = 2010;
// a: 存储合并过程中的前 n 个最小和，始终保持有序
// b: 当前正在读取的、等待与 a 合并的新数组
// c: 临时数组，用于暂存 a 和 b 合并后的前 n 个最小和
int n, m, a[N], b[N], c[N];

void merge() {
  priority_queue<PII, vector<PII>, greater<PII>> heap;
  for (int i = 0; i < n; i ++ ) heap.push({b[i] + a[0], 0});

  for (int i = 0; i < n; i ++ ) {
    auto t = heap.top(); heap.pop();
    int s = t.first, p = t.second;
    c[i] = s;
    // 既然 a[p] + b[i] 被取走了，那么对于当前的 b[i] 来说，
    // 下一个最小的潜在组合就是 a[p + 1] + b[i]
    heap.push({s - a[p] + a[p + 1], p + 1});
  }
  // 将合并后的前 n 个最小和复制回 a 数组
  for (int i = 0; i < n; i ++ ) a[i] = c[i];
}

// 将 m 个数组的合并问题，转化为 m-1 次两个数组的合并问题
// 因为a已有序，初始化时 b[0~n-1] 分别与 a[0] 结合形成 n 路（每一路都是从小到大）：
//   b[0] + a[0], b[0] + a[1], ..., b[0] + a[n-1]
//   b[1] + a[0], b[1] + a[1], ..., b[1] + a[n-1]
//   ...
//   b[n-1] + a[0], b[n-1] + a[1], ..., b[n-1] + a[n-1]
// 取 (n, n) 矩阵第一列入队作小根堆，取出最小值后，将取出元素那行的下一个元素入队
int main() {
  int T;
  cin >> T;
  while (T -- ) {
    cin >> m >> n;
    for (int i = 0; i < n; i ++ ) scanf("%d", &a[i]);
    sort(a, a + n); // 初始必须将 a 排序，这是 merge 逻辑成立的基础前提

    for (int i = 0; i < m - 1; i ++ ) { // 剩下的 m - 1 个数组，边读入边和 a 进行合并
      for (int j = 0; j < n; j ++ ) scanf("%d", &b[j]);
      merge(); // 合并 a 和 b，始终保留前 n 个最小的在 a 中
    }

    for (int i = 0; i < n; i ++ ) printf("%d ", a[i]);
    puts("");
  }

  return 0;
}