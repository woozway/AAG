#include <bits/stdc++.h>
using namespace std;
const int N = 1e4 + 10;
int n;
int x[N], y[N];

int work(int *q) { // 经典货仓选址：AcWing 104.
  sort(q, q + n);

  int res = 0;
  for (int i = 0; i < n; i ++ ) res += abs(q[i] - q[n / 2]);
  return res;
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i ++ ) cin >> x[i] >> y[i];

  // 士兵在 X 轴上不是汇聚到同一点，而是要“紧挨着排成一横排”
  // 为防止士兵在移动过程中相互交叉（交叉走肯定多绕路），
  // 必须先按照他们初始的 X 坐标从小到大排序，保证相对顺序不变
  sort (x, x + n);
  // 假设排好序的士兵，最终站立的连续 X 坐标分别是 k, k+1, k+2 ... k+(n-1)
  // 第 i 个士兵移动的距离是 |x[i] - (k + i)|，
  // 我们将其变形一下：|x[i] - (k + i)|  ===  |(x[i] - i) - k|
  // 这意味着，如果我们令新数组 x'[i] = x[i] - i，
  // 那么问题就转化为了：求 x' 数组中所有元素到一个点 k 的最小距离和
  for (int i = 0; i < n; i ++ ) x[i] -= i;

  // x 轴和 y 轴的移动是完全独立（正交）的，互不干扰
  cout << work(x) + work(y) << endl;
  return 0;
}