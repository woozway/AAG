#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 10;
int n;
char str[N]; // 字串下标从 1 开始，方便后续 KMP 算法找循环节
int nxt[N]; // nxt[i] 表示在字符串 str 中，最长的且相等的“真前缀”和“真后缀”的长度

void get_next() {
  // i 表示当前正在计算 nxt[i]，从 2 开始（因为 nxt[1] 是 0，单字符没有真前后缀）
  // j 表示当前匹配的最长公共前后缀的长度，同时也代表前缀的末尾下标
  for (int i = 2, j = 0; i <= n; i ++ ) {
    // 如果当前字符 str[i] 和 期望的前缀下一个字符 str[j + 1] 不匹配，
    // 则顺着失配指针 nxt[j] 不断回退，直到找到匹配的位置，或者退到 j = 0 为止
    while (j && str[i] != str[j + 1]) j = nxt[j];
    // 如果找到了匹配的字符，则最长公共前后缀长度 j 加 1
    if (str[i] == str[j + 1]) j ++ ;
    // 记录下当前前缀 str[1...i] 的最长公共前后缀长度
    nxt[i] = j;
  }
}

int main() {
  int T = 1;
  while (scanf("%d", &n), n) {
    scanf("%s", str + 1);

    get_next(); // 预处理求出整个字符串的 next 数组

    printf("Test case #%d\n", T ++ );
    // 枚举该字符串的所有前缀（长度从 2 开始，因为长度为 1 的前缀不可能有循环节）
    for (int i = 2; i <= n; i ++ ) {
      int t = i - nxt[i]; // KMP 性质：长度为 i 的串，其最小循环节长为 i - nxt[i]
      // 判断是否真的是循环节：
      // 1. i > t: 等价于 nxt[i] > 0。若 nxt[i] = 0，说明没有任何公共前后缀，t = i
      // 2. i % t == 0: 前缀总长度 i 必须能被最小循环节长度 t 整除
      if (i > t && i % t == 0) printf("%d %d\n", i, i / t);
    }
    puts("");
  }
  return 0;
}