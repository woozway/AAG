#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 2e5 + 10;
struct Seq {
  int s, e, d; // 定义等差数列结构体：s 为起点，e 为终点，d 为公差
} seqs[N];
int n;

LL get_sum(int x) { // 计算在所有数列中，小于等于 x 的数字总共有多少个
  LL res = 0;
  for (int i = 0; i < n; i ++ )
    if (seqs[i].s <= x) // 只有当数列的起点 s <= x 时，这个数列才可能包含 <= x 的数字
      res += (min(seqs[i].e, x) - seqs[i].s) / seqs[i].d + 1;
  return res;
}

int main() {
  int T;
  scanf("%d", &T);

  while (T -- ) {
    int l = 0, r = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ) {
      int s, e, d;
      scanf("%d%d%d", &s, &e, &d);
      seqs[i] = {s, e, d};
      r = max(r, e);
    }

    while (l < r) {
      int mid = (LL)l + r >> 1;
      if (get_sum(mid) & 1) r = mid;
      else l = mid + 1;
    }
    // 二分结束后 l == r，此时 r 就是那个唯一可能出现奇数次的数字
    auto sum = get_sum(r) - get_sum(r - 1);
    if (sum % 2) printf("%d %lld\n", r, sum);
    else puts("There's no weakness.");
  }

  return 0;
}