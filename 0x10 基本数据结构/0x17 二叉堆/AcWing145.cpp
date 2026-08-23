#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;

// 思路：按截止时间排序 + 最小堆（优先队列）维护收益
int main() {
  int n;
  while (cin >> n) {
    vector<PII> products(n); // <商品过期时间 (deadline), 商品利润 (profit)>
    for (int i = 0; i < n; i ++ ) cin >> products[i].second >> products[i].first;

    sort(products.begin(), products.end());

    // 堆顶是当前决定卖出的商品中，利润最小的那个；用一个高利润的商品去替换低利润的，总天数不变
    priority_queue<int, vector<int>, greater<int>> heap;
    for (auto p : products) {
      heap.push(p.second);
      if (heap.size() > p.first) heap.pop();
    }

    int res = 0;
    while (heap.size()) res += heap.top(), heap.pop();
    cout << res << endl;
  }

  return 0;
}