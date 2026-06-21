#include <bits/stdc++.h> // 用 unordered_set 需要自己写哈希
using namespace std;
typedef pair<int, int> PII;
const int N = 1e4 + 10;
int d[N], n, p, h, m;

// 每一对关系 AB 和其他关系 CD 没有交集（套娃，但边界点可能重合）
int main() {
  cin >> n >> p >> h >> m;
  d[1] = h; // 差分序列 d[1] = h 可以把所有牛的初始身高都变成 h

  set<PII> existed;
  for (int i = 0, a, b; i < m; i ++ ) {
    cin >> a >> b;
    if (a > b) swap(a, b);
    if (!existed.count({a, b})) {
      existed.insert({a, b});
      d[a + 1] -- , d[b] ++ ; // 将 [a + 1, b - 1] 的每个数减 1
    }
  }

  for (int i = 1; i <= n; i ++ ) { // 恢复原数组，d 上前缀和
    d[i] += d[i - 1];
    cout << d[i] << endl;
  }
  return 0;
}