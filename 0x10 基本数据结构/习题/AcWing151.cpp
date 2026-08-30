#include <bits/stdc++.h>
using namespace std;
stack<int> nums;
stack<char> ops;

int qmi(int a, int k) {
  int res = 1;
  while (k -- ) res *= a;
  return res;
}

void cal() {
  int a = nums.top(); nums.pop();
  int b = nums.top(); nums.pop();
  char c = ops.top(); ops.pop();
  int d;

  if (c == '+') d = b + a;
  else if (c == '-') d = b - a;
  else if (c == '*') d = b * a;
  else if (c == '/') d = b / a;
  else d = qmi(b, a);

  nums.push(d);
}

int main() {
  string str;
  cin >> str;

  if (str[0] == '-') str = '0' + str; // 预处理整个表达式以负号开头的情况
  string left; // 给表达式最左边拼上和表达式等长数量的 '('，最右边拼上一个 ')'
  for (int i = 0; i <= str.size(); i ++ ) left += '(';
  str = left + str + ')';

  for (int i = 0; i < str.size(); i ++ ) {
    if (isdigit(str[i])) {
      int j = i, t = 0;
      while (isdigit(str[j])) t = t * 10 + str[j ++ ] - '0';
      nums.push(t);
      i = j - 1;
    }
    else {
      char c = str[i];
      if (c == '(') ops.push(c);
      else if (c == '+' || c == '-') {
        // 判断当前的 '-' 是一元运算符（负号）还是二元运算符（减号）
        if (c == '-' && i && !isdigit(str[i - 1]) && str[i - 1] != ')') {
          if (str[i + 1] == '(') { // 将 -(...) 变成 -1 * (...)
            nums.push(-1);
            ops.push('*');
          }
          else {
            int j = i + 1, t = 0;
            while (isdigit(str[j])) t = t * 10 + str[j ++ ] - '0';
            nums.push(-t);
            i = j - 1;
          }
        }
        else { // 只要符号栈顶不是 '('，就说明前面的符号优先级全都 >= 加减号，统统算掉
          while (ops.top() != '(') cal();
          ops.push(c);
        }
      }
      else if (c == '*' || c == '/') { // 只有栈顶符号的优先级 >= 乘除时，才触发计算
        while (ops.top() == '*' || ops.top() == '/' || ops.top() == '^') cal();
        ops.push(c);
      }
      else if (c == '^') { // 这里实现了左结合律：如果栈顶也是 '^'，先算左边的 '^'
        while (ops.top() == '^') cal();
        ops.push(c);
      }
      else if (c == ')') { // 把当前括号内（遇到匹配的 '(' 之前）的所有算式全部算完
        while (ops.top() != '(') cal();
        ops.pop();
      }
      else cout << "invalid operator!" << endl;
    }
  }

  while(ops.size())
    if (ops.top() == '(') ops.pop();
    else cal();

  cout << nums.top() << endl;
  return 0;
}