#include <bits/stdc++.h>
using namespace std;
const int N = 1e4 + 10, M = 80;
int n, m;
char str[N][M]; // 存储二维字符矩阵，N 是行数，M 是列数
bool st[M]; // 状态数组：st[j] = true 表示宽度 j 能作为整个矩阵的横向循环节
int ne[N];

int main() {
  cin >> n >> m;

  memset(st, true, sizeof st);
  for (int i = 1; i <= n; i ++ ) {
    cin >> str[i];
    for (int j = 1; j <= m; j ++ ) { // 枚举候选宽度 j
      bool is_match = true;
      // 验证当前行是否能以 j 为周期循环，k 是后续循环块的起始位置（第一个块是 [0, j-1]）
      for (int k = j; k < m; k += j) {
        // u 是块内的偏移量，比较当前块与第一个块 [0, j-1] 的对应字符
        for (int u = 0; u < j && k + u < m; u ++ )
          // 如果后面的字符没有和第一个周期块 [0, j-1] 中的对应字符匹配
          if (str[i][u] != str[i][k + u]) {
            is_match = false;
            break;
          }
        if (!is_match) break;
      }
      if (!is_match) st[j] = false;
    }
  }

  int width;
  for (int i = 1; i <= m; i ++ )
    if (st[i]) {
      width = i; // 第一个没有被否定的 j，就是全局最小有效宽度
      break;
    }

  // 在每一行的第 width 个字符处放上 '\0'（字符串结束符）将整行字符串缩减成
  // 长度为 width 的基础循环块，可把“每一行”当作一个“超级字符”，用做 KMP 匹配
  for (int i = 1; i <= n; i ++ ) str[i][width] = 0;

  for (int j = 0, i = 2; i <= n; i ++ ) {
    while (j && strcmp(str[j + 1], str[i])) j = ne[j];
    if (!strcmp(str[j + 1], str[i])) j ++ ;
    ne[i] = j;
  }

  int height = n - ne[n]; // 长度为 n 的字符串，其最小循环节长度 = n - next[n]

  cout << width * height << endl;

  return 0;
}