#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 1e6 + 10;
int n;
LL s[N], c[N]; // s[] 前缀数组，c[] 偏移量数组

// b = (a1 + a2 + ... + an) / n，假设小朋友 1 号给 2 号 x1 个，n 号给 1 号 xn 个
// 可得：a_1 - x_1 + x_n = b, a_2 - x_2 + x_1 = b, ..., a_n - x_n + x_{n-1} = b
// 整理：x_1 = x_n - (b - a_1), x_2 = x_n - (2*b - a_1 - a_2), ...,
//      x_{n-1} = x_n - ((n-1)*b - a_1 - a_2 - ... - a_{n-1}), x_n = x_n - 0
// 此时，需要最小化：|x1| + |x2| + ... + |xn|，
// 即最小化：|x_n - (b - a_1)| + |x_n - (2*b - a_1 - a_2)| + ... + |x_n - 0|
// 由几何性质（距离）可得 x_n 为 n 个数的中位数
int main() {
  cin >> n;
  for (int i = 1; i <= n; i ++ ) {
    cin >> s[i];
    s[i] += s[i - 1];
  }

  LL b = s[n] / n;
  int k = 0;
  for (int i = 1; i < n; i ++ ) c[k ++ ] = i * b - s[i];
  c[k ++ ] = 0; // 对应公式中 x_n = x_n - 0 的基准点

  // sort(c, c + k);
  nth_element(c, c + k / 2, c + k);
  LL res = 0;
  for (int i = 0; i < k; i ++ ) res += abs(c[i] - c[k / 2]);

  cout << res << endl;
  return 0;
}