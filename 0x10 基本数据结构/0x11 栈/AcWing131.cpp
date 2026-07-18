#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 1e5 + 10;
int n;
int h[N], l[N], r[N], q[N]; // l/r 数组: 存储第 i 根柱子左/右边第一个高度严格小于它的柱子下标

int main() {
  while (cin >> n, n) {
    for (int i = 1; i <= n; i ++ ) cin >> h[i];
    h[0] = h[n + 1] = -1; // 哨兵：保证栈内永远有一个比所有正高度都小的值

    int tt = 0;
    q[0] = 0;
    for (int i = 1; i <= n; i ++ ) {
      while (h[i] <= h[q[tt]]) tt -- ;
      l[i] = q[tt];
      q[ ++ tt] = i;
    }

    tt = 0;
    q[0] = n + 1;
    for (int i = n; i; i -- ) {
      while (h[i] <= h[q[tt]]) tt -- ;
      r[i] = q[tt];
      q[ ++ tt] = i;
    }

    LL res = 0;
    for (int i = 1; i <= n; i ++ )
      res = max(res, (LL)h[i] * (r[i] - l[i] - 1));
    printf("%lld\n", res);
  }

  return 0;
}