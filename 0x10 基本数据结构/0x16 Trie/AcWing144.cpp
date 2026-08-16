#include <bits/stdc++.h>
using namespace std;
// N 是最大节点数，M 是最大边数（树是无向图，所以 M 是 N 的两倍）
const int N = 1e5 + 10, M = 2e5 + 10;
int n;
int h[N], e[M], c[M], ne[M], cnt = 1;
// a[i]: 存储节点 i 到根节点 (0号点) 的路径异或和
// son[3100000][2]: 01字典树：N=10万，每个数字31位，最多产生约 310万个节点
int a[N], son[3100000][2], idx;

void add(int u, int v, int w) {
  e[cnt] = v, c[cnt] = w, ne[cnt] = h[u], h[u] = cnt ++ ;
}

// 求出每个节点到根节点的异或和；fa: 父节点（防止回搜死循环）
void dfs(int u, int father, int sum) {
  a[u] = sum;
  for (int i = h[u]; i; i = ne[i]) {
    int j = e[i];
    if (j != father) dfs(j, u, sum ^ c[i]);
  }
}

void insert(int x) {
  int p = 0;
  for (int i = 30; i >= 0; i -- ) {
    int &s = son[p][x >> i & 1];
    // s 是一个引用，方便后续直接对其赋值（免去写 son[p][...] = ++idx 的繁琐）
    if (!s) s = ++ idx;
    p = s;
  }
}

int query(int x) {
  int p = 0, res = 0;
  for (int i = 30; i >= 0; i -- ) {
    int s = x >> i & 1;
    if (son[p][!s]) {
      res += 1 << i;
      p = son[p][!s];
    }
    else p = son[p][s];
  }
  return res;
}

int main() {
  cin >> n;
  for (int i = 0; i < n - 1; i ++ ) {
    int u, v, w;
    cin >> u >> v >> w;
    add(u, v, w);
    add(v, u, w);
  }

  dfs(0, -1, 0); // 初始化所有点到根节点（随便选一个作为根，这里选 0）的异或和

  for (int i = 0; i < n; i ++ ) insert(a[i]); // 把所有路径异或和 a[i] 插入到 Trie

  int res = 0; // 遍历所有的 a[i]，利用字典树贪心地找能和它产生最大异或和的另一个 a[j]
  for (int i = 0; i < n; i ++ ) res = max(res, query(a[i]));
  cout << res << endl;

  return 0;
}