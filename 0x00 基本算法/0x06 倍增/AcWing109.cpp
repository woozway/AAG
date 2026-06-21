#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 5e5 + 10;
int n, m, k, a[N], b[N], tmp[N]; // 必须引入 b，用于存储目前已经确立的、排好序的左半部分区间
LL t;

// 检查如果把区间从 mid 扩展到 r，新的这段区间 [l, r] 是否合法
bool check(int l, int mid, int r) {
  for (int i = mid + 1; i <= r; i ++ ) b[i] = a[i];
  sort(b + mid + 1, b + r + 1); // 将新步长的一截 [mid+1, r] 提取到 b 数组并单独排序

  int i = l, j = mid + 1; // 将 b[l~mid] 和 b[mid+1~r] 合并到 tmp
  for (int k = l; k <= r; k ++ )
    if (j > r || (i <= mid && b[i] <= b[j])) tmp[k] = b[i ++ ];
    else tmp[k] = b[j ++ ];

  LL sum = 0; // 贪心计算最大校验差的平方和
  for (int i = l, j = r; i < min(l + m, j); i ++ , j -- )
    sum += 1LL * (tmp[i] - tmp[j]) * (tmp[i] - tmp[j]);
  return sum <= t; // 这里绝对不能把 tmp 抄回 b，因为不知道是否合法
}

int main() {
  cin >> k;
  while (k -- ) {
    cin >> n >> m >> t;
    for (int i = 0; i < n; i ++ ) {
      cin >> a[i];
      b[i] = a[i];
    }

    int cnt = 0, l = 0;
    while (l < n) {
      int p = 1, r = l;
      while (p)
        if (r + p < n && check(l, r, r + p)) { // 试探将区间向右扩展 p 的长度
          r += p;
          for (int i = l; i <= r; i ++ ) b[i] = tmp[i]; // 成功，此时把合法的 tmp 更新回 b
          p <<= 1;
        }
        else p >>= 1; // 试探失败或越界，步长减半

      l = r + 1;
      cnt ++ ;
    }
    cout << cnt << endl;
  }
  return 0;
}