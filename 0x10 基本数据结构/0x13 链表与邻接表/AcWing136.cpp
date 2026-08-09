#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<LL, int> PLI;
const int N = 1e5 + 10;
int n;
int l[N], r[N]; // 双向链表
int p[N]; // p[k] = i 表示 [原数组中第 k 个输入的元素]，在 [排序后的数组 a] 中位于下标 i
PLI a[N], ans[N]; // a (first: 元素值, second: 原下标)

int main() {
  cin >> n;
  for (int i = 1; i <= n; i ++ ) {
    cin >> a[i].first;
    a[i].second = i;
  }
  sort(a + 1, a + 1 + n); // 排序后，值最接近的元素在数组中一定是相邻的

  a[0].first = -4e9, a[n + 1].first = 4e9; // 哨兵
  for (int i = 1; i <= n; i ++ ) {
    l[i] = i - 1, r[i] = i + 1;
    p[a[i].second] = i; // 后续可以 O(1) 找到任意原序列元素在链表里的位置
  }

  for (int i = n; i > 1; i -- ) { // 逆序求解
    int j = p[i], left = l[j], right = r[j];
    LL left_value = abs(a[left].first - a[j].first);
    LL right_value = abs(a[right].first - a[j].first);
    if (left_value <= right_value) ans[i] = {left_value, a[left].second};
    else ans[i] = {right_value, a[right].second};
    l[right] = left, r[left] = right; // 删除操作只需修改左右邻居的指针
  }

  for (int i = 2; i <= n; i ++ )
    cout << ans[i].first << ' ' << ans[i].second << endl;

  return 0;
}