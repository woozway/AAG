#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII; // <元素的绝对值, 节点在链表中的编号>
const int N = 1e5 + 10;
int n, m;
int a[N], l[N], r[N]; // a: 压缩合并后的正负段数值数组
bool st[N]; // 延迟删除标记：st[i] = true 表示节点 i 已从链表中删除

void remove(int p) {
  l[r[p]] = l[p];
  r[l[p]] = r[p];
  st[p] = true;
}

int main() {
  cin >> n >> m;

  // 合并后数组 a 呈现严格的正负交替状态：+ - + - + ...
  int k = 1;
  for (int i = 0; i < n; i ++ ) {
    int x;
    cin >> x;
    // 如果符号异号（乘积 < 0），存入新位置；否则累加到当前位置
    if ((long long)a[k] * x < 0) a[ ++ k] = x;
    else a[k] += x;
  }
  n = k; // 更新压缩后的段数

  // 假设默认选上所有的正数段
  int cnt = 0, res = 0; // cnt: 选中的正数段数量，res: 当前选中的总和
  for (int i = 1; i <= n; i ++ )
    if (a[i] > 0) {
      cnt ++ ;
      res += a[i];
    }

  priority_queue<PII, vector<PII>, greater<PII>> heap; // 小根堆：按绝对值
  for (int i = 1; i <= n; i ++ ) {
    l[i] = i - 1;
    r[i] = i + 1;

    heap.push({abs(a[i]), i});
  }

  // 反悔贪心：如果选中的正数段数量 cnt 超过了允许的最大选择数 m，两种操作
  // 两种操作效果都是 cnt - 1，代价都是 |a[p]|，所以按绝对值从小到大贪心地选代价小的操作：
  //   1. 放弃一个正数段（直接减去它的值，cnt - 1）
  //   2. 选一个负数段（承受它的代价，把左右两个正数段连起来，cnt - 1）
  while (cnt > m) {
    while (st[heap.top().second]) heap.pop();

    auto t = heap.top();
    heap.pop();

    // 如果 a[p] > 0（正数段）：可以直接放弃，有效
    // 如果 a[p] < 0（负数段）：需要左右都有正数段才能连接
    int v = t.first, p = t.second;
    if (l[p] != 0 && r[p] != n + 1 || a[p] > 0) {
      cnt -- ;
      res -= v; // 总和中减去代价（放弃正数 或 承受负数）

      // 合并：将左右邻居和当前段合并成一个新段：新段的值 = 左邻居 + 当前段 + 右邻居
      int left = l[p], right = r[p];
      a[p] += a[left] + a[right]; // 这样合并后，原来左右两个正数段被"连"起来了

      heap.push({abs(a[p]), p});
      remove(left);
      remove(right);
    }
  }

  cout << res << endl;

  return 0;
}