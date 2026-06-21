#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 500 * 500 + 10;
int n, a[N], tmp[N];

LL merge_sort(int l, int r) {
  if (l >= r) return 0;

  int mid = l + r >> 1;
  LL res = merge_sort(l, mid) + merge_sort(mid + 1, r);

  int i = l, j = mid + 1;
  for (int k = l; k <= r; k ++ )
    if (j > r || (i <= mid && a[i] <= a[j])) tmp[k] = a[i ++ ];
    else tmp[k] = a[j ++ ], res += mid - i + 1;

  for (int k = l; k <= r; k ++ ) a[k] = tmp[k];
  return res;
}

// 当网格列数 n 为奇数时，空格（数字 0）无论如何移动（上下左右），将网格
// 展平为一维序列后（忽略 0），整个序列的逆序对数量的奇偶性保持不变
// 扩展到 n 为偶数时，两个局面可达当且仅当两个局面对应网格写成序列后，
// “逆序对数之差”和“两个局面下空格所在的行数之差”奇偶行相同
int main() {
  while (cin >> n) {
    int cnt = 0; // 读入第一个局面并转化为一维（过滤 0）
    for (int i = 0; i < n * n; i ++ ) {
      int x; cin >> x;
      if (x != 0) a[cnt ++ ] = x;
    }
    LL res1 = merge_sort(0, cnt - 1); // 计算第一个局面的逆序对数

    cnt = 0; // 读入第二个局面
    for (int i = 0; i < n * n; i ++ ) {
      int x; cin >> x;
      if (x != 0) a[cnt ++ ] = x;
    }
    LL res2 = merge_sort(0, cnt - 1); // 计算第二个局面的逆序对数

    if ((res1 & 1) == (res2 & 1)) cout << "TAK" << endl;
    else cout << "NIE" << endl;
  }
  return 0;
}