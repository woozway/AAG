#include <bits/stdc++.h>
using namespace std;
typedef pair<string, int> PSI;
const int N = 1e5 + 10;
PSI p[N];
int n, m;

int calc(int bit, int now) {
  for (int i = 0; i < n; i++) {
    auto [op, x] = p[i];
    int b = x >> bit & 1;
    if (op == "AND") now &= b;
    else if (op == "OR") now |= b;
    else now ^= b;
  }
  return now;
}

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i ++ ) cin >> p[i].first >> p[i].second;

  int t = 0, res = 0; // 每位独立，贪心让伤害最大（每位上都倾向于选0，这样初始值才更有可能在m范围内）
  for (int i = 30; i >= 0; i -- ) { // 本题中m最大是10^9，lg2(10^9) = 3log2(10^3) < 30
    int a = calc(i, 0), b = calc(i, 1);
    if (t + (1 << i) <= m && a < b) t += 1 << i, res += b << i;
    else res += a << i;
  }
  cout << res << endl;
  return 0;
}