#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10; // 字典树的最大节点数（1e4 * 10）
int n;
int son[N][10], idx; // idx 用于给新产生的节点分配唯一编号，0 号节点既是根又是空节点
bool f[N]; // f[p] 标记数组，f[p] = true 表示节点 p 是某一个完整字符串的结尾

bool insert(char *str) {
  int p = 0;
  bool has_new = false; // 记录在插入这个字串的过程中，是否创建了新的节点
  bool has_found = false; // 记录在插入这个字串的路径上，是否经过某个之前已插入字串的结尾
  for (int i = 0; str[i]; i ++ ) {
    int u = str[i] - '0';
    if (!son[p][u]) {
      son[p][u] = ++ idx;
      has_new = true;
    }
    p = son[p][u];
    if (f[p]) has_found = true;
  }
  f[p] = true; // 循环结束，给当前字符串的最后一个节点打上结尾标记

  return has_new && !has_found; // “创建了新节点” 且 “没有路过别人家的结尾”
}

int main() {
  int T;
  cin >> T;
  while (T -- ) {
    cin >> n;
    memset(son, 0, sizeof son);
    memset(f, false, sizeof f);
    idx = 0;

    bool res = true; // 记录当前这组数据是否合法（默认没有前缀冲突）
    char str[20];
    while (n -- ) {
      cin >> str;
      if (!insert(str)) res = false;
    }

    if (res) puts("YES");
    else puts("NO");
  }

  return 0;
}