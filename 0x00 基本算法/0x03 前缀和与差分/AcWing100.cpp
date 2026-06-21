#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 1e5 + 10;
int n, a[N];

// b[l] += C, b[r + 1] -= C
// 1. 2 <= i, j <= n
// 2. i = 1, 2 <= j <= n
// 3. 2 <= i <= n, j = n + 1
// 4. i = 1, j = n + 1 无意义

// 先求差分数组 b：目标是把 b[2] ... b[n] 都变成 0；
// 然后统计 b 中正/负数的和，让他们最大程度地互相抵消
// 尽可能多选 1.，其他由 2. 和 3. 来补：
//   最少操作次数：min(pos, neg) + |pos - neg| = max(pos, neg)
//   最终数列个数：1. 可选：0 ~ |pos - neg|种方案
int main() {
  cin >> n;
  for (int i = 1; i <= n; i ++ ) cin >> a[i];
  for (int i = n; i > 1; i -- ) a[i] -= a[i - 1];

  LL pos = 0, neg = 0;
  for (int i = 2; i <= n; i ++ )
    if (a[i] > 0) pos += a[i];
    else neg -= a[i];

  cout << min(pos, neg) + abs(pos - neg) << endl;
  cout << abs(pos - neg) + 1 << endl;

  return 0;
}