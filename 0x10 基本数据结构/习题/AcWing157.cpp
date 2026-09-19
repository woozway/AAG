#include <bits/stdc++.h>
using namespace std;

// 解析当前子树，并返回该子树的“最小表示”（唯一标识字符串）
string dfs(string &seq, int &u) {
  u ++ ;
  vector<string> seqs; // 存储当前节点的所有子树的“最小表示”
  while (seq[u] == '0') seqs.push_back(dfs(seq, u));
  u ++ ; // 此时 seq[u] == '1'，跳过这个 '1'（退出当前节点）

  sort(seqs.begin(), seqs.end()); // 对所有子树的表示字符串进行字典序排序

  // 组装当前这棵子树的最终表示，格式为："0" + (所有子树的最小表示按字典序拼接) + "1"
  string res = "0";
  for (auto &s : seqs) res += s;
  res += '1';
  return res;
}

int main() {
  int T;
  cin >> T;
  while (T -- ) {
    string a, b;
    cin >> a >> b;

    // 加虚拟根节点，保证整个序列是一棵单一完整的大树，一次 dfs() 就能全部解析完
    a = '0' + a + '1';
    b = '0' + b + '1';
    int ua = 0, ub = 0; // 初始化遍历指针
    auto ra = dfs(a, ua), rb = dfs(b, ub);

    if (ra == rb) puts("same");
    else puts("different");
  }
  return 0;
}