#include <bits/stdc++.h>
using namespace std;
const int N = 5e5 + 10, M = 1e6 + 10; // N 代表字典树中节点的最大数量
int n, m;
char str[M];
// son[p][s]: 存储节点 p 的所有子节点。s 的范围是 0~25 (代表 a~z)
//            它的值是指向的下一个节点的编号。如果为 0，代表该子节点不存在
// cnt[p]: 标记以节点 p 结尾的字符串个数
// idx: 节点编号分配器，表示当前用到了哪个节点。0 号节点既是根节点，也是空节点
int son[N][26], cnt[N], idx;

void insert() {
  int p = 0;
  for (int i = 0; str[i]; i ++ ) {
    int t = str[i] - 'a';
    if (!son[p][t]) son[p][t] = ++ idx;
    p = son[p][t];
  }
  cnt[p] ++ ;
}

int query() {
  int p = 0, res = 0;
  for (int i = 0; str[i]; i ++ ) {
    int t = str[i] - 'a';
    if (!son[p][t]) break;
    p = son[p][t];
    res += cnt[p];
  }
  return res;
}

int main() {
  scanf("%d%d", &n, &m);
  while (n -- ) {
    scanf("%s", str);
    insert();
  }

  while (m -- ) {
    scanf("%s", str);
    printf("%d\n", query());
  }
  return 0;
}