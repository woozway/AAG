#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 10;
int stkl[N], stkr[N], topl, topr; // 对顶栈：stkl/stkr 分别存储光标左/后边的元素
int f[N], sum[N]; // sum[i]: 左栈中前 i 个元素前缀和；f[i]: 左栈中前 i 个元素里，最大的前缀和

void add(int x) { // 在光标处（左栈顶）插入一个新元素
  stkl[ ++ topl] = x;
  sum[topl] = sum[topl - 1] + x;
  f[topl] = max(f[topl - 1], sum[topl]);
}

int main() {
  int n;
  scanf("%d", &n);

  f[0] = INT_MIN; // 初始状态没有元素，最大子段和设为极小值（防止全负数时出错）
  char ops[2]; // 用字符串读取单个字符，可以自动过滤掉空格和换行符
  while (n -- ) {
    int x;
    scanf("%s", ops);
    if (*ops == 'I') {
      scanf("%d", &x);
      add(x);
    }
    else if (*ops == 'D') {
      if (topl) topl -- ;
    }
    else if (*ops == 'L') {
      if (topl) stkr[ ++ topr] = stkl[topl -- ];
    }
    else if (*ops == 'R') {
      // stkr 可以在频繁的 LLLLRRRLLR 时保存光标左右的上下文
      if (topr) add(stkr[topr -- ]);
    }
    else {
      scanf("%d", &x);
      printf("%d\n", f[x]);
    }
  }
  return 0;
}