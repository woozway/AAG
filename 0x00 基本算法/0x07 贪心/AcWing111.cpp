#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;
const int N = 5e4 + 10;
int n, id[N]; // id：记录每头牛（按原始输入顺序）最终分配到的畜栏编号
pair<PII, int> cows[N]; // cows：pair<pair<开始时间, 结束时间>, 输入的原始序号>

int main() {
  cin >> n;
  for (int i = 0; i < n; i ++ ) {
    cin >> cows[i].first.first >> cows[i].first.second;
    cows[i].second = i;
  }

  sort(cows, cows + n); // 按牛的开始吃草时间从早到晚排序

  priority_queue<PII, vector<PII>, greater<PII>> heap; // minheap，<畜栏的结束时间，畜栏编号>
  for (int i = 0; i < n; i ++ )
    if (heap.empty() || heap.top().first >= cows[i].first.first) {
      PII stall = {cows[i].first.second, heap.size()}; // 需要新开一个畜栏
      id[cows[i].second] = stall.second; // 利用牛的“身份证”找回它原本的位置，为它分配畜栏编号
      heap.push(stall);
    }
    else { // 贪心：复用现有畜栏，直接把这头牛塞进最早空出来的畜栏里
      auto stall = heap.top(); heap.pop();
      stall.first = cows[i].first.second; // 用新加入的cow[i]的结束时间更新该畜栏的结束时间
      id[cows[i].second] = stall.second;
      heap.push(stall);
    }

  cout << heap.size() << endl;
  for (int i = 0; i < n; i ++ ) cout << id[i] + 1 << endl; // 畜栏编号从 1 开始
  return 0;
}