#include <bits/stdc++.h>
using namespace std;
const int N = 2e6 + 10;
int n;
char a[N], b[N];

int get_min(char str[]) { // 求字符串的最小表示法的起始下标
  int i = 0, j = 1; // i 和 j 是两个候选的起始位置，初始时错开
  while (i < n && j < n) {
    int k = 0; // k 表示当前从 i 和 j 开始，能够匹配的相同字符的长度
    while (k < n && str[i + k] == str[j + k]) k ++ ;
    if (k == n) break; // 如果 k 达到 n，说明字符串有循环节，或两个候选位置完全相同

    if (str[i + k] > str[j + k]) i += k + 1;
    else j += k + 1;

    if (i == j) i ++ ;
  }
  int res = min(i, j); // 最小的那个起始位置就是答案
  str[res + n] = 0;
  return res;
}

int main() {
  scanf("%s%s", a, b);
  n = strlen(a);

  memcpy(a + n, a, n); // 破环成链
  memcpy(b + n, b, n);

  int ia = get_min(a), ib = get_min(b); // 分别求出 a 和 b 的最小表示法的起始位置

  if (strcmp(a + ia, b + ib)) puts("No");
  else {
    puts("Yes");
    puts(a + ia);
  }

  return 0;
}