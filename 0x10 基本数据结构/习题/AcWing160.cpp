#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10;
int n, m, q;
char a[N], b[N]; // a: 主串, b: 模式串 (下标均从 1 开始)
int ne[N];
int f[N]; // 频率数组: f[i] 最终表示模式串 b 的前缀 b[1...i] 在主串 a 中出现的总次数

int main() {
  cin >> n >> m >> q;
  scanf("%s%s", a + 1, b + 1);

  // 预处理模式串 b 的 next 数组
  for (int i = 2, j = 0; i <= m; i ++ ) {
    while (j && b[i] != b[j + 1]) j = ne[j];
    if (b[i] == b[j + 1]) j ++ ;
    ne[i] = j;
  }

  // 每处理完 a[i]，j 就表示"以 a[i] 结尾的子串，与 b 的前缀最长能匹配多长"
  for (int i = 1, j = 0; i <= n; i ++ ) {
    while (j && a[i] != b[j + 1]) j = ne[j];
    if (a[i] == b[j + 1]) j ++ ;
    // 例如 j=5 时，说明 b[1..5] 被完整匹配了，但 b[1..ne[5]] 其实也隐式被匹
    // 配了（因为它是 b[1..5] 的后缀），这里还没加上去，留到下一步统一处理
    f[j] ++ ; // f[j] 记录"最长匹配长度恰好为 j"的出现次数
  }

  // 倒序遍历，把长前缀的频次"传递"给它的父节点（短前缀）如果 b[1...i] 出现了
  // f[i] 次，那么 b[1...ne[i]] 也至少额外出现了 f[i] 次（作为 b[1...i] 的后缀）
  for (int i = m; i; i -- ) f[ne[i]] += f[i];

  // f[x]     = b[1...x]   在 a 中出现的总次数（匹配长度 >= x 的次数）
  // f[x + 1] = b[1...x+1] 在 a 中出现的总次数（匹配长度 >= x+1 的次数）
  // f[x] - f[x + 1] 就是"匹配长度恰好为 x"的次数
  while (q -- ) {
    int x;
    cin >> x;
    cout << f[x] - f[x + 1] << endl;
  }

  return 0;
}