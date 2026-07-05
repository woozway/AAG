#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII; // pair<存储时间 x，存储等级 y>
const int N = 1e5 + 10;
int n, m;
PII mchs[N], tasks[N];

int main() {
  while (cin >> n >> m) {
    for (int i = 0; i < n; i ++ ) cin >> mchs[i].first >> mchs[i].second;
    for (int i = 0; i < m; i ++ ) cin >> tasks[i].first >> tasks[i].second;

    sort(mchs, mchs + n);
    sort(tasks, tasks + m);

    multiset<int> ys; // ys 用于动态存储 [当前满足时间要求] 的所有机器的“等级(y)”
    LL cnt = 0, res = 0;
    // 优先处理时间长、等级高的任务：倒序遍历 tasks，从大到小挑
    for (int i = m - 1, j = n - 1; i >= 0; i -- ) {
      int x = tasks[i].first, y = tasks[i].second;
      // 如果一台机器的时间能满足当前耗时长的任务，那它必然也能满足后面耗时短的任务
      // 所以我们用指针 j，把所有时间满足当前任务的机器，统统扔进机器池 ys 中
      while (j >= 0 && mchs[j].first >= x) ys.insert(mchs[j -- ].second);
      // 为了把高等级的机器留给后面可能需要高等级的任务，我们应该选 [刚好能胜任] 的机器
      // lower_bound(y)：在池子里找第一个等级 >= 当前任务所需等级 y 的机器
      auto it = ys.lower_bound(y);
      if (it != ys.end()) {
        cnt ++ ;
        res += 500 * x + 2 * y;
        ys.erase(it); // 这台机器被征用了，从可用机器池中删去
      }
    }
    cout << cnt << ' ' << res << endl;
  }
  return 0;
}