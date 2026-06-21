#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
const int N = 2510;
int n, m;
PII cows[N]; // 存储每头牛对防晒霜的区间要求 [minSPF, maxSPF]

// 按牛的 minSPF 从大到小（逆序）分配：因为 minSPF 越大的牛，能用的防晒霜下限越高，属于“最挑剔”的牛。需优先满足它们
// 为当前牛分配能用的防晒霜中，SPF值最大的一款：对于一头牛，只要防晒霜的 SPF 在它的 [minSPF, maxSPF] 范围内即可
// 为了给后续 minSPF 较小的牛留下尽可能多的选择，当前这头牛应该尽量用掉 SPF 偏大的防晒霜
int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i ++ ) cin >> cows[i].first >> cows[i].second;

  map<int, int> spfs; // map 会自动按键值从小到大排序：<防晒霜的 SPF 值, 剩余瓶数>
  for (int i = 0; i < m; i ++ ) {
    int spf, cover;
    cin >> spf >> cover;
    spfs[spf] += cover; // 注意可能有多种防晒霜 SPF 值相同，所以要累加瓶数
  }

  sort(cows, cows + n); // 将牛按 minSPF 从小到大排序

  int res = 0;
  spfs[0] = spfs[1001] = n; // 1 <= spf <= 1000, spfs[0] 防止迭代器一直自减退到 begin() 之前越界
                            // spfs[1001] 防止 upper_bound 找不到大于 maxSPF 的值时迭代器自减崩溃
  for (int i = n - 1; i >= 0; i -- ) { // 倒序遍历，优先处理 minSPF 最大的牛
    auto spf = spfs.upper_bound(cows[i].second);
    spf -- ; // 迭代器退后一步，此时 spf 指向的必然是 <= 当前牛 maxSPF 的 "最大 SPF 值"
    if (spf->first >= cows[i].first && spf->first <= cows[i].second) {
      res ++ ;
      if (-- spf->second == 0)
        spfs.erase(spf); // 直接从 map 中删去，避免干扰后续其他牛的二分查找
    }
  }

  cout << res << endl;
  return 0;
}