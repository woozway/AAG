#include <iostream>
using namespace std;

int qmi(int a, int b, int p) {
  a %= p; // 用long long会超时，这里不用；基数a也需要取模p
  int res = 1 % p;
  while (b) {
    if (b & 1) res = res * a % p;
    a = a * a % p;
    b >>= 1;
  }
  return res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int t;
  cin >> t;
  while (t -- ) {
    int res = 0;
    int p, n;
    cin >> p >> n;
    while (n -- ) {
      int a, b;
      cin >> a >> b;
      res = (res + qmi(a, b, p)) % p;
    }
    cout << res << endl;
  }
  return 0;
}