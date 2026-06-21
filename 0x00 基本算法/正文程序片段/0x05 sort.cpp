// 离散化
void discrete() {
  sort(a + 1, a + n + 1);
  for (int i = 1; i <= n; i ++ ) // 也可用 STL 中的 unique 函数
    if (i == 1 || a[i] != a[i - 1])
      b[ ++ m] = a[i];
}

// 离散化后，查询 x 映射为哪个 1 ~ m 之间的整数
void query(int x) {
  return lower_bound(b + 1, b + m + 1, x) - b;
}


// 归并排序求逆序对
void merge(int l, int mid, int r) {
  // 合并 a[l ~ mid] 与 a[mid + 1 ~ r]
  // a 是待排序数组, b 是临时数组, cnt 是逆序对个数
  int i = l, j = mid + 1;
  for (int k = l; k <= r; k ++ )
    if (j > r || i <= mid && a[i] <= a[j]) b[k] = a[i ++ ];
    else b[k] = a[j ++ ], cnt += mid - i + 1;
  for (int k = l; k <= r; k ++ ) a[k] = b[k];
}
