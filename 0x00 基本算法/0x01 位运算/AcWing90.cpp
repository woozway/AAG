#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int main() {
  LL a, b, p;
  cin >> a >> b >> p;

  LL res = 0;
  while (b) {
    if (b & 1) res = (res + a) % p;
    a = (a + a) % p;
    b >>= 1;
  }
  cout << res << endl;
  return 0;
}