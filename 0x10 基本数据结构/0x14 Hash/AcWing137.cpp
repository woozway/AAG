#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
int n;
int snows[N][6]; // snows 存储每片雪花最终计算出的“唯一身份证”（字典序最小的 6 位序列）
int idx[N]; // idx 存储雪花的编号 0 ~ n-1，用于“间接排序”，避免直接交换庞大的数组

void get_min(int *b) { // 找出环形数组中字典序最小的起始位置，并将原数组更新为这个最小序列
  static int a[12];
  for (int i = 0; i < 12; i ++ ) a[i] = b[i % 6]; // 将长度为 6 的数组复制一倍拼在后面

  int i = 0, j = 1, k; // i 和 j 是两个候选的起始位置，k 是当前它们能够匹配的长度
  while (i < 6 && j < 6) {
    for (k = 0; k < 6 && a[i + k] == a[j + k]; k ++ ) ;
    if (k == 6) break; // 说明出现了完全相同的循环节，直接结束

    // 如果 a[i+k] > a[j+k]，说明以 i 开头的序列肯定不如以 j 开头的序列小
    // 不仅如此，对于任何 0 <= p <= k，以 i+p 开头的序列，都一定不如以 j+p 开头的序列小
    // 因此，i 到 i+k 这一段作为起始位置全都被淘汰，i 直接跳到 i + k + 1
    if (a[i + k] > a[j + k]) {
      i += k + 1;
      if (i == j) i ++ ; // i 和 j 不能在同一个位置比，如果重合了，i 再往后挪一步
    }
    else { // 反之亦然，如果 a[i+k] < a[j+k]，淘汰 j 到 j+k 这一段
      j += k + 1;
      if (i == j) j ++ ;
    }
  }

  k = min(i, j); // 循环结束后，i 和 j 中较小的那个，就是字典序最小的起始位置
  for (i = 0; i < 6; i ++ ) b[i] = a[i + k]; // 将这个字典序最小序列覆盖回原数组 b 中
}

bool cmp2(int a[], int b[]) { // 比较两个长度 6 的数组，若 a 的字典序小于 b，返回 true
  for (int i = 0; i < 6; i ++ )
    if (a[i] != b[i]) return a[i] < b[i];
  return false;
}

bool cmp(int a, int b) { // 通过 idx 数组间接比较 snows 中的雪花身份证
  return cmp2(snows[a], snows[b]);
}

int main() {
  scanf("%d", &n);
  int snow[6], isnow[6]; // isnow 记录对应的逆时针序列
  for (int i = 0; i < n; i ++ ) {
    for (int j = 0, k = 5; j < 6; j ++ , k -- ) {
      scanf("%d", &snow[j]);
      isnow[k] = snow[j];
    }
    get_min(snow);
    get_min(isnow);

    // 将这两者中字典序更小的那个，拷贝到全局数组 snows[i] 中
    if (cmp2(snow, isnow)) memcpy(snows[i], snow, sizeof snow);
    else memcpy(snows[i], isnow, sizeof isnow);
    idx[i] = i; // 记录原始编号，用于间接排序，以减少内存拷贝开销
  }

  sort(idx, idx + n, cmp); // 排序后，如果存在相同雪花，它们的身份证在数组中必定相邻
  for (int i = 1; i < n; i ++ ) // 检查相邻的两个雪花是否相同
    if (!cmp(idx[i], idx[i - 1]) && !cmp(idx[i - 1], idx[i])) {
      puts("Twin snowflakes found.");
      return 0;
    }

  puts("No two snowflakes are alike.");
  return 0;
}