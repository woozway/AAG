#include <bits/stdc++.h>
using namespace std;
const int N = 3e4 + 10;
int n, m;
int a[N], b[N];

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i ++ ) cin >> a[i];
  for (int i = 0; i < m; i ++ ) cin >> b[i];

  sort(b, b + m); // 必须保证查询时刻 b 是有序的（按照加入元素的数量升序排列）

  priority_queue<int> left; // 大根堆，维护当前序列中排在第 1 到第 i-1 小的元素
  priority_queue<int, vector<int>, greater<int>> right; // 第 i 到最大值的所有元素

  // i：当前已向黑盒中加入的元素数量 a[0...i-1]；j：当前处理到第几个 GET 查询 b[j]
  int i = 0, j = 0;
  while (i < n || j < m) {
    // GET 操作
    while (j < m && b[j] == i) { // 当已放入黑盒的元素数量达到 b[j] 时，触发 GET 查询
      cout << right.top() << endl;
      left.push(right.top());
      right.pop();
      j ++ ;
    }
    if (i >= n) break;
    // ADD 操作
    int x = a[i];
    // 如果 x 大于等于 right 的最小值，说明 x 属于“较大的一半”，直接放入小根堆 right
    if (left.empty() || x >= right.top()) right.push(x);
    else {
      left.push(x);
      right.push(left.top());
      left.pop();
    }
    i ++ ;
  }

  return 0;
}