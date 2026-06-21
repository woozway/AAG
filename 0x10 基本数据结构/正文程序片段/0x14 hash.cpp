// 字符串 Hash：取固定值 P 和 M，把字符串看作 P 进制数，P 一般取 131 或 13331，哈希冲突概率低
// 求出该 P 进制数对 M 的余数，作为该字符串 Hash 值
// 例：S="abc", c="d", T="xyz"，令a=1, b=2, ..., z=26
//  S 表示为P进制数：1 2 3
//  H(S) = 1*P^2 + 2*P + 3
//  H(S+c) = 1*P^3 + 2*P^2 + 3*P + 4 = H(S)*P + 4
//  S+T 表示为 P 进制数：1 2 3 24 25 26
//  H(S+T) = 1*P^5 + 2*P^4 + 3*P^3 + 24*P^2 + 25*P + 26
//  S 在 P 进制下左移 length(T) 位：1 2 3 0 0 0
//  二者相减就是 T 表示为 P 进制数：24 25 26
//  H(T) = H(S+T) - (1*P^2 + 2*P + 3) * P^3 = 24*P^2 + 25*P + 26
// 根据上述操作，可 O(N) 处理字符串所有前缀 Hash 值，在 O(1) 时间内查询其任意子串的 Hash 值

// Hash 例题：兔子与兔子
char s[1000010];
unsigned long long f[1000010], p[1000010];
int n, q;
int main() {
  scanf("%s", s + 1);
  n = strlen(s + 1);
  cin >> q;
  p[0] = 1; // 131^0
  for (int i = 1; i <= n; i ++ ) {
    f[i] = f[i - 1] * 131 + (s[i] - 'a' + 1); // hash of 1~i
    p[i] = p[i - 1] * 131; // 131^i
  }
  for (int i = 1; i <= q; i ++ ) {
    int l1, r1, l2, r2;
    scanf("%d%d%d%d", &l1, &r1, &l2, &r2);
    if (f[r1] - f[l1 - 1] * p[r1 - l1 + 1] == // hash of l1~r1
      f[r2] - f[l2 - 1] * p[r2 - l2 + 1]) { // hash of l2~r2
      puts("Yes");
    } else {
      puts("No");
    }
  }
}