#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
int n, a[N], f[N]; // 后缀最小值数组：f[i] 表示 a[i...n] 中的最小值
int color[N]; // 节点颜色：-1 表示未染色，0 表示分配到栈 1，1 表示分配到栈 2
bool g[N][N]; // 邻接矩阵：g[i][j] = true 表示元素 a[i] 和 a[j] 不能放入同一个栈

// 二分图染色
bool dfs(int u, int c) {
  color[u] = c;
  for (int i = 1; i <= n; i++)
    if (g[u][i]) {
      if (color[i] == c) return false;
      if (color[i] == -1 && !dfs(i, !c)) return false;
    }
  return true;
}

int main() {
  cin >> n;
  for (int i = 1; i <= n; i ++ ) cin >> a[i];

  // 预处理后缀最小值
  f[n + 1] = n + 1;
  for (int i = n; i; i -- ) f[i] = min(f[i + 1], a[i]);

  // 建图：判断任意两元素 a[i] 和 a[j] 是否不能在同一个栈中
  // 条件：i < j 且 a[i] < a[j]，并且存在 k > j 满足 a[k] < a[i]
  // 借助后缀最小值数组，即转化为：a[i] < a[j] && f[j + 1] < a[i]
  memset(g, false, sizeof g);
  for (int i = 1; i <= n; i ++ )
    for (int j = i + 1; j <= n; j ++ )
      if (a[i] < a[j] && f[j + 1] < a[i])
        g[i][j] = g[j][i] = true;

  // 优先将未染色的点染成 0（对应栈 1），以保证最终操作序列的字典序最小
  memset(color, -1, sizeof color);
  bool flag = true;
  for (int i = 1; i <= n; i ++ )
    if (color[i] == -1 && !dfs(i, 0)) {
      flag = false; // 出现奇环，无法划分为两个独立的栈
      break;
    }

  if (!flag) {
    cout << 0 << endl;
    return 0;
  }

  stack<int> stk1, stk2;
  int now = 1; // 当前期望输出的目标数值 (1, 2, ..., n)
  int i = 1; // 当前等待处理的输入数组下标
  while (now <= n) { // 按 a -> b -> c -> d 顺序贪心选择合法操作
    // 操作 a：将当前元素入 stk1 (前提：颜色为 0 且满足单调栈性质/栈顶大于当前值)
    if (i <= n && color[i] == 0 && (stk1.empty() || stk1.top() > a[i])) {
      stk1.push(a[i ++ ]);
      cout << "a ";
    }
    // 操作 b：将 stk1 栈顶弹出 (前提：栈顶值正好等于当前期望输出的数值 now)
    else if (stk1.size() && stk1.top() == now) {
      stk1.pop();
      now ++ ;
      cout << "b ";
    }
    // 操作 c：将当前元素入 stk2 (前提：颜色为 1 且满足单调栈性质/栈顶大于当前值)
    else if (i <= n && color[i] == 1 && (stk2.empty() || stk2.top() > a[i])) {
      stk2.push(a[i ++ ]);
      cout << "c ";
    }
    // 操作 d：将 stk2 栈顶弹出 (前提：栈顶值正好等于当前期望输出的数值 now)
    else if (stk2.size() && stk2.top() == now) {
      stk2.pop();
      now ++ ;
      cout << "d ";
    }
  }
  cout << endl;

  return 0;
}