#include <bits/stdc++.h>
using namespace std;
const int mod = 9901;

int qmi(int a, int b, int p) {
  a %= p;
  int res = 1 % p;
  while (b) {
    if (b & 1) res = res * a % p;
    a = a * a % p;
    b >>= 1;
  }
  return res;
}

// 如果k是偶数：
// sum(p, k) = p^0 + p^1 + ... + p^k
//           = p^0 + p * (p^0 + p^1 + ... + p^(k-1))
//           = 1 + p * sum(p, k - 1)
// 如果k是奇数：
// sum(p, k) = p^0 + p^1 + ... + p^k
//           = (p^0 + .. + p^(k/2)) + (p^(k/2 + 1) + .. + p^k)
//           = (p^0 + .. + p^(k/2)) + p^(k/2 + 1) * (p^0 + .. + p^(k/2))
//           = (1 + p^(k/2 + 1)) * sum(p, k / 2)
int sum(int p, int k) {
  if (k == 0) return 1;
  if (k % 2 == 0) return (1 + p % mod * sum(p, k - 1) % mod) % mod;
  return (1 + qmi(p, k / 2 + 1, mod)) % mod * sum(p, k / 2) % mod;
}

// 对A分解质因数：A = p1^k1 * p2^k2 * ... * pn^kn
// 约数个数：(k1 + 1) * (k2 + 1) * ... * (kn + 1)
// 约数之和：(p1^0 + p1^1 +...+ p1^n) * (p2^0 +...+ p2^n) *...* (pn^0 +...+ pn^n)
int main() {
  int A, B;
  cin >> A >> B;

  int res = 1;
  for (int i = 2; i <= A / i; i ++ ) {
    int s = 0;
    while (A % i == 0) s ++ , A /= i;
    if (s) res = res * sum(i, s * B) % mod;
  }
  if (A > 1) res = res * sum(A, 1 * B) % mod; 

  if (!A) res = 0;
  cout << res << endl;
  return 0;
}