#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 1e5 + 10;
int n, m, t, row[N], col[N];
LL s[N], c[N];

// 见 AcWing 122. 糖果传递
LL calc(int n, int a[]) {
  for (int i = 1; i <= n; i ++ ) s[i] = s[i - 1] + a[i];
  if (s[n] % n != 0) return -1; // 判断是否能够均分

  LL b = s[n] / n;
  int k = 0;
  for (int i = 1; i < n; i ++ ) c[k ++ ] = i * b - s[i];
  c[k ++ ] = 0;

  nth_element(c, c + k / 2, c + k); // sort(c, c + k);
  LL res = 0;
  for (int i = 0; i < n; i ++ ) res += abs(c[i] - c[k / 2]);
  return res;
}

int main () {
  cin >> n >> m >> t;
  while (t -- ) {
    int x, y;
    cin >> x >> y;
    row[x] ++ , col[y] ++ ;
  }

  LL res1 = calc(n, row), res2 = calc(m, col); // 行和列完全正交，互不干扰，分别计算
  if (res1 != -1 && res2 != -1) cout << "both " << res1 + res2 << endl;
  else if (res1 != -1) cout << "row " << res1 << endl;
  else if (res2 != -1) cout << "column " << res2 << endl;
  else puts("impossible");
  return 0;
}