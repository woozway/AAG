typedef long long LL;
typedef unsigned long long ULL;

// 快速幂，求 a^b mod p
int power(int a, int b, int p) {
  int ans = 1;
  for (; b; b >>= 1) {
    if (b & 1) ans = (LL)ans * a % p;
    a = (LL)a * a % p;
  }
  return ans;
}

// 64 位整数乘法的 O(log b) 算法
LL mul(LL a, LL b, LL p) {
  LL ans = 0;
  for (; b; b >>= 1) {
    if (b & 1) ans = (ans + a) % p;
    a = a * 2 % p;
  }
  return ans;
}

// 64 位整数乘法的 long double 算法
ULL mul(ULL a, ULL b, ULL p) {
  a %= p, b %= p;  // 当 a, b 一定在 0 ~ p 之间时，此行不必要
  ULL c = (long double)a * b / p;
  ULL x = a * b, y = c * p;
  LL ans = (LL)(x % p) - (LL)(y % p);
  if (ans < 0) ans += p;
  return ans;
}

// hamilton 路径
int f[1 << 20][20];
int hamilton(int n, int weight[20][20]) {
  memset(f, 0x3f, sizeof(f));
  f[1][0] = 0;
  for (int i = 1; i < 1 << n; i ++ )
    for (int j = 0; j < n; j ++ )
      if (i >> j & 1)
        for (int k = 0; k < n; k ++ )
          if (i >> k & 1)
            f[i][j] = min(f[i][j], f[i ^ 1 << j][k] + weight[k][j]);
  return f[(1 << n) - 1][n - 1];
}

// lowbit 运算，找到二进制下所有是 1 的位
int H[37];
// 预处理
for (int i = 0; i < 36; i ++ ) H[(1ll << i) % 37] = i;
// 对多次询问进行求解
while (cin >> n) {
  while (n > 0) {
    cout << H[(n & -n) % 37] << ' ';
    n -= n & -n;
  }
  cout << endl;
}