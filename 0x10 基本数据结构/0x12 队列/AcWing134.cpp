#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;
const int N = 2e5 + 10;
int n;
PII a[N]; // a[i] 存储（元素的值，该元素在原数组中的下标）

// 将按值排好序的元素，根据其原始下标，划分为最少数量的“V型（先降后升）”段落
int main() {
  cin >> n;
  for (int i = 0; i < n; i ++ ) {
    cin >> a[i].first;
    a[i].second = i;
  }
  sort(a, a + n); // 值相同的元素不仅排在一起，而且它们的原始下标天然是递增的
  int res = 1;
  // last 记录上一个合法元素的原始下标。初始设为 n+1 (无穷大)，方便开启第一次递减
  // dir 记录当前的延伸方向：-1 表示原下标递减阶段，1 表示原下标递增阶段
  for (int i = 0, last = n + 1, dir = -1; i < n; ) {
    int j = i; // 将所有值相同的元素作为一个整体批次来处理（因为值相同元素的相对顺序无所谓）
    while (j < n && a[j].first == a[i].first) j ++ ;
    // minx 是这批相同值中，原下标最小的；maxx 是原下标最大的
    int minx = a[i].second, maxx = a[j - 1].second;
    
    if (dir == -1) {
      if (last > maxx) last = minx;
      else dir = 1, last = maxx;
    }
    else {
      if (last < minx) last = maxx;
      else {
        res ++ ;
        last = minx;
        dir = -1;
      }
    }
    i = j; // 跳过这批处理完的相同值，处理下一批
  }

  cout << res << endl;
  return 0;
}