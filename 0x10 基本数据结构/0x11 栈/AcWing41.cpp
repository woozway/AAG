class MinStack {
public:
  /** initialize your data structure here. */

  stack<int> stk, stk_min; // stk_min：辅助栈，栈顶始终保存当前数据栈中最小值

  MinStack() {

  }

  void push(int x) {
    stk.push(x);
    if (stk_min.size()) x = min(x, stk_min.top());
    stk_min.push(x);
  }

  void pop() {
    stk.pop();
    stk_min.pop();
  }

  int top() {
    return stk.top();
  }

  int getMin() {
    return stk_min.top();
  }
};