#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
const int N = 10010;

int main() {
  int T;
  cin >> T;
  while (T -- ) {
    int m, n;
    cin >> m >> n;
    priority_queue<int> max_heap; // max_heap 存储较小的一半数字
    priority_queue<int, vector<int>, greater<int>> min_heap;

    printf("%d %d\n", m, (n + 1) / 2);
    int cnt = 0;
    for (int i = 0; i < n; i ++ ) {
      int t;
      scanf("%d", &t);
      max_heap.push(t); // 默认先把新数扔进大根堆，动态中位数放在 max_heap 里
      if (min_heap.size() && min_heap.top() < max_heap.top()) {
        auto a = min_heap.top(), b = max_heap.top();
        min_heap.pop(), max_heap.pop();
        min_heap.push(b), max_heap.push(a);
      }

      if (max_heap.size() > min_heap.size() + 1) {
        min_heap.push(max_heap.top());
        max_heap.pop();
      }

      if (!(i & 1)) {
        printf("%d ", max_heap.top());
        if ( ++ cnt % 10 == 0) puts("");
      }
    }

    if (cnt % 10) puts(""); // 最后一行如果不满10个，也要补一个换行符
  }

  return 0;
}