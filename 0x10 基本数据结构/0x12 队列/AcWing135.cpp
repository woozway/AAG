#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 3e5 + 10;
int n, m;
LL s[N];
int q[N]; // q 数组模拟双端单调队列，用来存放前缀和的下标

int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i ++ ) {
    scanf("%lld", &s[i]);
    s[i] += s[i - 1];
  }

  LL res = LLONG_MIN;
  int hh = 0, tt = 0; // 初始时 q[0] = 0, 下标 0 代表前缀和 s[0] = 0，初始状态
  for (int i = 1; i <= n; i ++ ) {
    if (q[hh] < i - m) hh ++ ; // 检查队头是否滑出窗口，合法范围：[i - m, i - 1]
    res = max(res, s[i] - s[q[hh]]);
    while (hh <= tt && s[q[tt]] >= s[i]) tt -- ;
    q[ ++ tt] = i;
  }

  printf("%lld\n", res);
  return 0;
}