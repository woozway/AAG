#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;
const int N = 1010;
int n;
PII p[N]; // pair<存 a * b (用于排序)，存 a (左手数字，用于累乘)>

vector<int> mul(vector<int> &A, int b) {
  vector<int> C;
  for (int i = 0, t = 0; i < A.size() || t; i ++ ) {
    if (i < A.size()) t += A[i] * b;
    C.push_back(t % 10);
    t /= 10;
  }
  while (C.size() > 1 && C.back() == 0) C.pop_back();
  return C;
}

vector<int> div(vector<int> &A, int b, int &r) {
  vector<int> C;
  r = 0;
  for (int i = A.size() - 1; i >= 0; i -- ) {
    r = r * 10 + A[i];
    C.push_back(r / b);
    r %= b;
  }

  reverse(C.begin(), C.end());
  while (C.size() > 1 && C.back() == 0) C.pop_back();
  return C;
}

vector<int> max_vec(vector<int> A, vector<int> B) { // 比较两个高精度数字大小，返回较大的
  if (A.size() > B.size()) return A;
  if (A.size() < B.size()) return B;
  if (vector<int>(A.rbegin(), A.rend()) > vector<int>(B.rbegin(), B.rend())) return A;
  return B;
}

int main() {
  cin >> n;
  for (int i = 0; i <= n; i ++ ) {
    int a, b;
    cin >> a >> b;
    p[i] = {a * b, a};
  }
  sort(p + 1, p + n + 1); // 按 a * b 的值对大臣进行排序（国王 p[0] 不参与）

  vector<int> product(1, 1); // product 用于记录当前排在前面所有人的左手数字之积
  vector<int> res(1, 0); // res 用于记录全场最大奖赏值，初值 0
  int r;
  for (int i = 0; i <= n; i ++ ) {
    if (i) res = max_vec(res, div(product, p[i].first / p[i].second, r));
    product = mul(product, p[i].second);
  }

  for (int i = res.size() - 1; i >= 0; i -- ) cout << res[i];
  cout << endl;
  return 0;
}