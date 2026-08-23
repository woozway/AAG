#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<LL, int> PLI; // <当前线段长度（两点间距离）, 该线段在数组中原始下标位置>
const int N = 1e5 + 10;
int n, k;
int l[N], r[N];
LL d[N]; // d: 初始存储输入的点坐标，随后原地转换为相邻两点之间的距离

void delete_node(int p) {
  r[l[p]] = r[p];
  l[r[p]] = l[p];
}

int main() {
  cin >> n >> k;

  for (int i = 0; i < n; i ++ ) cin >> d[i];
  for (int i = n - 1; i; i -- ) d[i] -= d[i - 1]; // 倒序

  set<PLI> S; // S 用于维护当前所有可选线段的最小值
  d[0] = d[n] = 1e15; // 距离的有效下标是 1 ~ n-1，哨兵节点设置0,n
  for (int i = 0; i <= n; i ++ ) {
    l[i] = i - 1;
    r[i] = i + 1;
    S.insert({d[i], i});
  }

  LL res = 0;
  while (k -- ) {
    auto it = S.begin();
    LL v = it->first;
    int p = it->second, left = l[p], right = r[p];

    // 选了 p，按“不能相邻”规则，从 set 中把当前节点及其左右邻居彻底删掉
    S.erase(it);
    S.erase({d[left], left}), S.erase({d[right], right});
    // 从链表中把左右邻居删掉，p 节点保留，作为后续“反悔”的占位符
    delete_node(left), delete_node(right);
    res += v;

    // 往原位置 p 插入一个全新的“反悔节点”
    d[p] = d[left] + d[right] - d[p];
    S.insert({d[p], p});
  }

  cout << res << endl;
  return 0;
}