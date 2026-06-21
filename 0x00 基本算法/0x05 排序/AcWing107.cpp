#include <bits/stdc++.h>
typedef long long LL;
using namespace std;
const int N = 5e5 + 10;
int n, a[N], tmp[N];

LL merge_sort(int l, int r) {
  if (l >= r) return 0;

  int mid = l + r >> 1;
  LL res = merge_sort(l, mid) + merge_sort(mid + 1, r);

  int i = l, j = mid + 1;
  for (int k = l; k <= r; k ++ )
    if (j > r || i <= mid && a[i] <= a[j]) tmp[k] = a[i ++ ];
    else tmp[k] = a[j ++ ], res += mid - i + 1;

  for (int k = l; k <= r; k ++ ) a[k] = tmp[k];

  return res;
}

int main() {
  while (cin >> n && n) {
    for (int i = 1; i <= n; i ++ ) cin >> a[i];
    cout << merge_sort(1, n) << endl;
  }
  return 0;
}