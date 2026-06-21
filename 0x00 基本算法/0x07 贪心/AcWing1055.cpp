#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
int n, p[N];

// 缩小求解空间：可将跨越天数>1的交易拆分成若干个跨越天数为1的交易；n-1个交易互相独立
int main() {
  cin >> n;
  for (int i = 0; i < n; i ++ ) cin >> p[i];

  int res = 0;
  for (int i = 0; i < n - 1; i ++ ) res += max(0, p[i + 1] - p[i]);

  cout << res;
  return 0;
}