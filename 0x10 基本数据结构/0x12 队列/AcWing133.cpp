#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10, M = 7e6 + 10;
int n, m, q, u, v, t;
int q1[N], q2[M], q3[M]; // q1 存蚯蚓初始长度（降序）；q2/q3 存每次切割后按比例分成的第一/二段
int delta; // delta: 全局偏移量，用于记录所有蚯蚓总共增长了多少长度
int hh1, hh2, hh3, tt1, tt2 = -1, tt3 = -1;

int get_max() { // 从三个队列的队头中，找出最大的那个元素并出队，返回其“相对长度”
  int x = INT_MIN;
  if (hh1 <= tt1) x = max(x, q1[hh1]);
  if (hh2 <= tt2) x = max(x, q2[hh2]);
  if (hh3 <= tt3) x = max(x, q3[hh3]);
  if (hh1 <= tt1 && x == q1[hh1]) hh1 ++ ;
  else if (hh2 <= tt2 && x == q2[hh2]) hh2 ++ ;
  else hh3 ++ ;
  return x;
}

// 隐藏的单调性（先被切开的蚯蚓，产生的两段一定比后被切开的蚯蚓产生的两段更长）
int main() {
  scanf("%d%d%d%d%d%d", &n, &m, &q, &u, &v, &t);
  for (int i = 0; i < n; i ++ ) scanf("%d", &q1[i]);
  sort(q1, q1 + n);
  reverse(q1, q1 + n);
  tt1 = n - 1;
  
  for (int i = 1; i <= m; i ++ ) {
    int x = get_max(); // 拿到当前所有蚯蚓中最长的一条（相对长度）
    x += delta; // 加上全局偏移量 delta，恢复成当前的真实长度
    if (i % t == 0) printf("%d ", x);
    int left = x * 1ll * u / v; // 乘法前先转 long long，防止 x * u 在相乘时整型溢出
    int right = x - left;
    delta += q; // 注意新切出的两段，不会参与这一秒的自然增长
    left -= delta, right -= delta; // 将新切出来的两段放入 q2 和 q3
    q2[ ++ tt2] = left, q3[ ++ tt3] = right;
  }
  puts("");

  for (int i = 1; i <= n + m; i ++ ) {
    int x = get_max();
    if (i % t == 0) printf("%d ", x + delta);
  }
  puts("");
  return 0;
}