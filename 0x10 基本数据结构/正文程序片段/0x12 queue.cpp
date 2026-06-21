// 单调队列
int l = 1, r = 1;
q[1] = 0; // save choice j=0
for (int i = 1; i <= n; i ++ ) {
  while (l <= r && q[l] < i - m) l ++ ; // 判断队头与i的距离是否超出m，超出则出队
  ans = max(ans, sum[i] - sum[q[l]]); // 此时队头就是右端点为i时，左端点j的最佳选择
  while (l <= r && sum[q[r]] >= sum[i]) r -- ; // 不断删除队尾，直到其s小于s[i]
  q[ ++ r] = i; // 然后新决策（下标）入队
}