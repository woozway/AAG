// 递归法求中缀表达式的值，O(n^2)
int calc(int l, int r) {
  // 寻找未被任何括号包含的最后一个加减号。j=0 表示肯定在括号外面，因为 j-- 和 j++ 对应
  for (int i = r, j = 0; i >= l; i -- ) {
    if (s[i] == '(') j ++ ;
    if (s[i] == ')') j -- ;
    if (j == 0 && s[i] == '+') return calc(l, i - 1) + calc(i + 1, r);
    if (j == 0 && s[i] == '-') return calc(l, i - 1) - calc(i + 1, r);
  }
  // 寻找未被任何括号包含的最后一个乘除号。这里先找+-再*/因为后者优先级更高
  for (int i = r, j = 0; i >= l; i -- ) {
    if (s[i] == '(') j ++ ;
    if (s[i] == ')') j -- ;
    if (j == 0 && s[i] == '*') return calc(l, i - 1) * calc(i + 1, r);
    if (j == 0 && s[i] == '/') return calc(l, i - 1) / calc(i + 1, r);
  }
  // 首尾是括号
  if (s[l] == '(' && s[r] == ')') return calc(l + 1, r - 1);
  // 是一个数
  int ans = 0;
  for (int i = l; i <= r; i ++ ) ans = ans * 10 + s[i] - '0';
  return ans;
}

// ----------------------------------------------------
// 中缀表达式转后缀表达式，同时求值，O(n)
vector<int> nums; // 数值栈
vector<char> ops; // 运算符栈

// 优先级 
int grade(char op) {
  switch (op) {
  case '(':
    return 1;
  case '+':
  case '-':
    return 2;
  case '*':
  case '/':
    return 3;
  }
  return 0;
}

// 处理后缀表达式中的一个运算符 
void calc(char op) {
  // 从栈顶取出两个数 
  int y = *nums.rbegin(); nums.pop_back();
  int x = *nums.rbegin(); nums.pop_back();
  int z;
  switch (op) {
  case '+': z = x + y; break;
  case '-': z = x - y; break;
  case '*': z = x * y; break;
  case '/': z = x / y; break;
  }
  // 把运算结果放回栈中 
  nums.push_back(z);	
}

// 中缀表达式转后缀表达式，同时对后缀表达式求值 
int solve(string s) {
  nums.clear();
  ops.clear();
  int top = 0, val = 0;
  for (int i = 0; i < s.size(); i ++ ) {
    // 中缀表达式的一个数字 
    if (s[i] >= '0' && s[i] <= '9') {
      val = val * 10 + s[i] - '0';
      if (s[i + 1] >= '0' && s[i + 1] <= '9') continue;
      // 后缀表达式的一个数，直接入栈 
      nums.push_back(val);
      val = 0;
    }
    // 中缀表达式的左括号 
    else if (s[i] == '(') ops.push_back(s[i]);
    // 中缀表达式的右括号 
    else if (s[i] == ')') {
      while (*ops.rbegin() != '(') {
        // 处理后缀表达式的一个运算符 
        calc(*ops.rbegin());
        ops.pop_back();
      }
      ops.pop_back();
    }
    // 中缀表达式的加减乘除号 
    else {
      while (ops.size() && grade(*ops.rbegin()) >= grade(s[i])) {
        calc(*ops.rbegin());
        ops.pop_back();
      }
      ops.push_back(s[i]);
    } 
  }
  while (ops.size()) {
    calc(*ops.rbegin());
    ops.pop_back();
  }
  // 后缀表达式栈中最后剩下的数就是答案 
  return *nums.begin();
}

// ----------------------------------------------------
// 单调栈
a[n + 1] = p = 0; // 首末尾增加高度为0的矩形，以免扫描结束后栈中有剩余
for (int i = 1; i <= n + 1; i ++ ) {
  if (a[i] > s[p]) {
    s[ ++ p] = a[i], w[p] = 1; // s是栈，p是栈顶指针top，w[p]是对应矩阵宽度
  } else {
    int width = 0;
    while (s[p] > a[i]) { // 这里必须是>，否则因为a[n+1]=0时会越界
      width += w[p];
      ans = max(ans, (long long)width * s[p]);
      p -- ;
    }
    s[ ++ p] = a[i], w[p] = width + 1;
  }
}
