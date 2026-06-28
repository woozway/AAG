#include <bits/stdc++.h>
using namespace std;
vector<int> closed[14]; // closed 数组用来存放 13 堆尚未翻开（背面朝上）的牌
int open[14]; // open 数组用来记录每一堆“已经正面朝上”翻开的牌的数量

int main() {
  for (int i = 1; i <= 13; i ++ )
    for (int j = 0; j < 4; j ++ ) {
      int x;
      char s[2];
      cin >> s;
      if (*s >= '2' && *s <= '9') x = *s - '0';
      else if (*s == '0') x = 10;
      else if (*s == 'A') x = 1;
      else if (*s == 'J') x = 11;
      else if (*s == 'Q') x = 12;
      else x = 13;
      closed[i].push_back(x);
    }

  // 游戏从第 13 堆（K 堆）开始作为初始动力池。第 13 堆一共 4 张牌，所以发起 4 轮连锁
  for (int i = 0; i < 4; i ++ ) {
    int t = closed[13][i];
    while (t != 13) {
      open[t] ++ ; // 把刚抽到的牌 t 放到对应的第 t 堆上，该堆翻开的牌数 +1
      int r = t;
      t = closed[r].back(); // 从第 r 堆的顶部（最后存入的牌）抽出一张新的未翻开的牌，赋值给 t
      closed[r].pop_back();
    }
  }

  int res = 0;
  for (int i = 1; i <= 12; i ++ ) res += open[i] >= 4;
  cout << res << endl;
  return 0;
}