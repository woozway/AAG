#include <bits/stdc++.h>
using namespace std;

int main() {
  string str;
  cin >> str;
  stack<int> stk;

  int res = 0;
  for (int i = 0; i < str.size(); i ++ ) {
    char c = str[i];
    if (c == ')' && stk.size() && str[stk.top()] == '(') stk.pop();
    else if (c == ']' && stk.size() && str[stk.top()] == '[') stk.pop();
    else if (c == '}' && stk.size() && str[stk.top()] == '{') stk.pop();
    else stk.push(i);

    // 如果栈不空，那么从 stk.top() + 1 到 i 这一段，一定是一个合法括号子串
    // 如果栈为空，说明合法的长度就是从整个字符串的开头 0 到当前位置 i
    if (stk.size()) res = max(res, i - stk.top());
    else res = max(res, i + 1);
  }

  cout << res << endl;
  return 0;
}