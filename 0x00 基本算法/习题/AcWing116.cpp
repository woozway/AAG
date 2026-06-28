#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
const int N = 4;
int change[N][N]; // change[i][j]：当点击 (i, j) 位置时，受影响的所有格子的“二进制状态掩码”

int get(int x, int y) {
  return x * N + y; // 将 4x4 矩阵的二维坐标 (x, y) 映射为 0~15 的一维编号
}

int main() {
  // 预处理操作掩码：计算点击每个位置 (i, j) 会影响哪些格子
  for (int i = 0; i < N; i ++ )
    for (int j = 0; j < N; j ++ ) {
      for (int k = 0; k < N; k ++ ) change[i][j] += (1 << get(i, k)) + (1 << get(k, j));
      change[i][j] -= 1 << get(i, j); // 在上面的循环中，交叉点 (i, j) 被加了两次，需要去重
    }

  int state = 0; // 读取初始状态，压缩成一个 16 位的整数 state
  for (int i = 0; i < N; i ++ ) {
    string line;
    cin >> line;
    for (int j = 0; j < N; j ++ )
      if (line[j] == '+') // '+' 视为 1 (闭合需要被翻转)，'-' 视为 0 (目标状态)
        state += 1 << get(i, j);
  }

  vector<PII> path, temp;
  for (int i = 0; i < 1 << 16; i ++ ) { // 每一个整数 i 的二进制表示，就代表了一种点击方案
    int now = state;
    temp.clear();
    for (int j = 0; j < 16; j ++ ) // 遍历这 16 个格子，看看当前方案 i 打算按哪些格子
      if (i >> j & 1) {
        int x = j / 4, y = j % 4;
        now ^= change[x][y]; // 用now 异或上预处理好的操作掩码 change[x][y]，完成一行一列的翻转
        temp.push_back({x, y});
      }
    if (!now && (path.empty() || path.size() > temp.size())) path = temp;
  }

  cout << path.size() << endl;
  for (auto &p : path)
    cout << p.first + 1 << ' ' << p.second + 1 << endl;

  return 0;
}