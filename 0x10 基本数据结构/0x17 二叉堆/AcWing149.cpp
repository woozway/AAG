#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<LL, int> PLI; // <当前子树的权重之和, 当前树的深度>
const int N = 1e5 + 10;

int main() {
  int n, m;
  cin >> n >> m;

  priority_queue<PLI, vector<PLI>, greater<PLI>> heap;
  for (int i = 0; i < n; i ++ ) {
    LL w;
    cin >> w;
    heap.push({w, 0}); // 初始时，每个单词都是一个叶子节点，深度为 0
  }

  while ((n - 1) % (m - 1)) heap.push({0ll, 0}), n ++ ; // 补零

  LL res = 0;
  while (heap.size() > 1) {
    LL sum = 0;
    int depth = 0;
    for (int i = 0; i < m; i ++ ) {
      sum += heap.top().first;
      depth = max(depth, heap.top().second);
      heap.pop();
    }
    res += sum;
    heap.push({sum, depth + 1}); // 新节点的深度 = 最大子树深度 + 1
  }
  cout << res << endl << heap.top().second << endl;

  return 0;
}