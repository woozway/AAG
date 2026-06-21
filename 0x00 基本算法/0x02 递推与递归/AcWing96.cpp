#include <bits/stdc++.h>
using namespace std;
const int N = 15;
int d[N], f[N]; // d[n]/f[n]分别表示求解该n盘3/4塔问题的最少步数

int main() {
  d[0] = 0;
  for (int i = 1; i <= 12; i ++ ) d[i] = d[i - 1] + 1 + d[i - 1];

  memset(f, 0x3f, sizeof f);
  f[0] = 0;
  for (int i = 1; i <= 12; i ++ )
    for (int j = 0; j < i; j ++ )
      f[i] = min(f[i], f[j] + d[i - j] + f[j]);

  for (int i = 1; i <= 12; i ++ ) cout << f[i] << endl;
  return 0;
}