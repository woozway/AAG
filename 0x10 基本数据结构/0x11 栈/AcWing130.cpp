#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 6e6 + 10, M = 1.2e5 + 10;
LL res[N], tt; // res 存高精度结果数组（倒序存放），tt 是最高位的下标
int q[M]; // q[i] 存质数 i 在最终结果中的指数（幂次）
bool st[M]; // 埃氏筛中标记是否为合数

void mul(int b) {
  LL t = 0;
  for (int i = 0; i <= tt; i ++ ) {
    res[i] = res[i] * b + t;
    t = res[i] / 1000000000;
    res[i] %= 1000000000;
  }
  while (t) {
    res[ ++ tt] = t % 1000000000;
    t /= 1000000000;
  }
}

// 勒让德定理：求 n!（n的阶乘）中包含质因子 p 的最高次幂
int get(int n, int p) {
  int s = 0;
  while (n) s += n / p, n /= p;
  return s;
}

// 将出栈序列 -> '+'/'-'序列 -> 路径问题（非法路径必定经过：y = x + 1，将该非法
// 路径与 y = x + 1 的第一个交点后的路径关于 y = x + 1 做轴对称，最后到达 (n-1, n+1) 点），
// 那么可以将 (0, 0) -> (n, n) 的一条非法路径和一条 (0,0) -> (n-1, n+1) 一一对应
// Catlan 数：任意前缀中，sum('-') <= sum('+')：C(2n,n) - C(2n,n-1) = C(2n,n)/(n+1)
int main() {
  int n;
  cin >> n;
  // 找出 2 到 2n 之间的所有质数
  for (int i = 2; i <= 2 * n; i ++ )
    for (int j = i + i; j <= 2 * n; j += i)
      st[j] = true;

  // 根据 C(2n,n) = (2n)! / (n!*n!)，质数 i 在 (2n)! 中的幂次减去在两个 n! 中的幂次
  for (int i = 2; i <= n * 2; i ++ )
    if (!st[i])
      q[i] = get(n * 2, i) - get(n, i) * 2;

  int k = n + 1;
  for (int i = 2; i <= k; i ++ )
    while (k % i == 0) {
      k /= i;
      q[i] -- ;
    }

  // 高精度乘法（数组初始化为 1）：将所有质因子按照它们最终的幂次 q[i] 乘起来
  res[0] = 1;
  for (int i = 2; i <= n * 2; i ++ )
    while (q[i] -- )
      mul(i);
  // 压位高精度输出：最高位正常输出（没有前导0）
  printf("%lld", res[tt]);
  for (int i = tt - 1; i >= 0; i -- ) printf("%09lld", res[i]);
  cout << endl;

  return 0;
}