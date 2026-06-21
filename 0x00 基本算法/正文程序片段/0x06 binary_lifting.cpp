// 区间最值问题的 ST 算法
// f[i][j] 表示 [i, i + (1<<j) - 1] 区间内 (1 << j) 个数的最大值
// 长度为 1 << j 的子区间的最大值是左右两半长度为 1 << (j-1) 的最大值中的较大一个
// f[i][j] = max(f[i][j - 1], f[i + (1 << (j - 1))][j - 1])
void ST_prework() {
  for (int i = 1; i <= n; i ++ ) f[i][0] = a[i]; // 边界
  int t = log(n) / log(2) + 1;
  for (int j = 1; j < t; j ++ )
    // n - (n - (1 << j) + 1) + 1 = 1 << j
    for (int i = 1; i <= n - (1 << j) + 1; i ++ )
      f[i][j] = max(f[i][j - 1], f[i + (1 << (j - 1))][j - 1]);
}

int ST_query(int l, int r) {
  // 先计算出 k，满足：(1 << k) <= r - l + 1 < (1 << (k + 1))
  int k = log(r - l + 1) / log(2);
  // 从 l 开始 1 << k 个数，和以 r 结尾的 1 << k 个数，这两段一定覆盖区间 [l, r]
  // 即区间 [l, l + (1 << k) - 1] 和 [r - (1 << k) + 1, r]
  return max(f[l][k], f[r - (1 << k) + 1][k]);
}