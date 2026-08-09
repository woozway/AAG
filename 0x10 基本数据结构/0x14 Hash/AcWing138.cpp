#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ULL; // 等价于对 2^64 取模
const int N = 1e6 + 10, p = 131; // p 是哈希的进制基数
char str[N];
ULL h[N], power[N]; // h[i] 存储字符串前 i 个字符的哈希

ULL get(int l, int r) { // 计算并返回子串 str[l...r] 的哈希值
  return h[r] - h[l - 1] * power[r - l + 1];
}

int main() {
  scanf("%s", str + 1); // h[0] 默认为 0，避免了数组越界的麻烦
  int n = strlen(str + 1);

  power[0] = 1;
  for (int i = 1; i <= n; i ++ ) { // 预处理前缀哈希数组 h 和次方数组 power
    h[i] = h[i - 1] * p + str[i] - 'a' + 1;
    power[i] = power[i - 1] * p;
  }

  int m;
  scanf("%d", &m);
  while (m -- ) {
    int l1, r1, l2, r2;
    scanf("%d%d%d%d", &l1, &r1, &l2, &r2);
    if (get(l1, r1) == get(l2, r2)) puts("Yes");
    else puts("No");
  }
  return 0;
}