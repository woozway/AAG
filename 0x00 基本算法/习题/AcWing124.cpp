#include <bits/stdc++.h>
using namespace std;

int main() {
  int T;
  cin >> T;
  while (T -- ) {
    int a, b;
    string a_line;
    cin >> a >> b >> a_line;

    vector<int> number;
    for (auto c : a_line)
      if (c <= '9') number.push_back(c - '0');
      else if (c <= 'Z') number.push_back(c - 'A' + 10);
      else number.push_back(c - 'a' + 36);

    reverse(number.begin(), number.end());

    vector<int> res;
    // 高精度短除法（除基取余）：只要这个大整数还没有被完全除尽，就继续除以 b
    while (number.size()) {
      int t = 0; // t 用来暂存高位向下传递的余数
      for (int i = number.size() - 1; i >= 0; i -- ) {
        number[i] += t * a;
        t = number[i] % b;
        number[i] /= b;
      }
      res.push_back(t);
      while (number.size() && !number.back()) number.pop_back();
    }

    reverse(res.begin(), res.end()); // 余数倒过来
    string b_line;
    for (auto x : res)
      if (x <= 9) b_line += char('0' + x);
      else if (x <= 35) b_line += char('A' + x - 10);
      else b_line += char('a' + x - 36);

    cout << a << ' ' << a_line << endl;
    cout << b << ' ' << b_line << endl;
    cout << endl;
  }
  return 0;
}