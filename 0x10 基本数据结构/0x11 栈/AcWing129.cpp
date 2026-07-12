#include <bits/stdc++.h>
using namespace std;
int n, remain = 20;
vector<int> path; // path: 记录当前已经出栈的元素，即最终的出栈序列
stack<int> stk;

void dfs(int u) { // 参数 u: 表示当前正在等待进栈的数字（1 ~ n）
  if (!remain) return;
  if (path.size() == n) {
    remain -- ;
    for (auto x : path) cout << x;
    cout << endl;
    return;
  }

  if (stk.size()) { // 为保证输出的出栈序列是字典序最小的，须优先选择“出栈”
    path.push_back(stk.top());
    stk.pop();
    dfs(u); // 此时等待进栈的数字仍然是 u，所以传参还是 u
    stk.push(path.back()); // 恢复现场（回溯）
    path.pop_back();
  }
  if (u <= n) { // 执行进栈操作
    stk.push(u);
    dfs(u + 1); // 数字 u 已经进栈，下一个等待进栈的数字变成了 u + 1
    stk.pop();
  }
}

int main() {
  cin >> n;
  dfs(1);
  return 0;
}