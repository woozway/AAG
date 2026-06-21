// 1. 递归版本
#include <bits/stdc++.h>
using namespace std;
int n, m;

void dfs(int u, int sum, int state) {
  // 0:
  if (sum + n - u < m) return ;
  if (sum == m) {
    for (int i = 0; i < n; i ++ )
      if (state >> i & 1) cout << i + 1 << ' ';
    cout << endl;
    return ;
  }

  dfs(u + 1, sum + 1, state + (1 << u));

  // 1:
  dfs(u + 1, sum, state);

  // 2:
}

int main() {
  cin >> n >> m;

  dfs(0, 0, 0);

  return 0;
}

// // 2. 非递归版本
// #include <bits/stdc++.h>
// using namespace std;
// struct State {
//   int pos, u, sum, state; // pos 对应 dfs 中的 0,1,2 位置
// };
// int n, m;

// int main() {
//   cin >> n >> m;

//   stack<State> stk;
//   stk.push({0, 0, 0, 0});

//   while (stk.size()) {
//     auto t = stk.top();
//     stk.pop();

//     if (t.pos == 0) {
//       if (t.sum + n - t.u < m) continue;
//       if (t.sum == m) {
//         for (int i = 0; i < n; i ++ )
//           if (t.state >> i & 1) cout << i + 1 << ' ';
//         cout << endl;
//         continue;
//       }

//       t.pos = 1; // 标记当前任务：下次回来时，该执行 pos=1 的逻辑了
//       stk.push(t); // 把“待办事项”压回栈底
//       stk.push({0, t.u + 1, t.sum + 1, t.state + (1 << t.u)}); // 把“选当前数字”的新状态压入栈顶（深度优先，先执行它）
//     }
//     else if (t.pos == 1) {
//       t.pos = 2;
//       stk.push(t);
//       stk.push({0, t.u + 1, t.sum, t.state});
//     }
//     else continue;
//   }

//   return 0;
// }