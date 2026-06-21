#include <bits/stdc++.h>
using namespace std;
const int N = 6e5 + 10, M = 2e5 + 10; // 离散化科学家会的语言+电影的语音&字幕：n + 2m = 6e5
int n, m, a[N], b[M], c[M]; // a[] 离散化后每种语言的科学家人数，b[] 语音编号，c[] 字幕编号
vector<int> all, add; // add 单独存一份科学家的语言，方便后面统计频率

int find(int x) { // 分成：(...), (x, ...) 两部分
  int l = 0, r = all.size() - 1;
  while (l < r) {
    int mid = l + r >> 1;
    if (all[mid] < x) l = mid + 1;
    else r = mid;
  }
  return l + 1;
}

int main() {
  cin >> n;
  while (n -- ) {
    int x; cin >> x;
    all.push_back(x);
    add.push_back(x);
  }

  cin >> m;
  for (int i = 1; i <= m; i ++ ) {
    cin >> b[i];
    all.push_back(b[i]);
  }
  for (int i = 1; i <= m; i ++ ) {
    cin >> c[i];
    all.push_back(c[i]);
  }

  sort(all.begin(), all.end());
  all.erase(unique(all.begin(), all.end()), all.end());

  for (auto i : add) a[find(i)] ++ ; // 统计每种语言的科学家数量

  int res = 1, Like = 0, like = 0;
  for (int i = 1; i <= m; i ++ ) {
    int L = a[find(b[i])], l = a[find(c[i])];
    if (Like < L) Like = L, like = l, res = i;
    else if (Like == L && like < l) like = l, res = i;
  }

  cout << res << endl;
  return 0;
}