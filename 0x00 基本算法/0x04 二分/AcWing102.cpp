#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
int cows[N], n, m;
double sum[N];

// 寻找 cow[] 数组中是否存在一个长度至少为 m 的连续子段，其平均值 >= avg
bool check(double avg) {
  for (int i = 1; i <= n; i ++ )
    sum[i] = sum[i - 1] + (cows[i] - avg);

  double mins = 0;
  for (int i = m, j = 0; i <= n; i ++, j ++ ) {
    mins = min(mins, sum[j]); // 记录并更新历史最小的前缀和
    if (sum[i] - mins >= 0) return true;
  }
  return false;
}

int main() {
  cin >> n >> m;
  double l = 0, r = 0;
  for (int i = 1; i <= n; i ++ ) {
    cin >> cows[i];
    r = max(r, (double)cows[i]);
  }

  while (r - l > 1e-5) { // 因为最后r*1000，保留k=3位小数，eps=10e-(k+2)
    double mid = (l + r) / 2;
    if (check(mid)) l = mid;
    else r = mid;
  }

  printf("%d\n", (int)(r * 1000));
  return 0;
}