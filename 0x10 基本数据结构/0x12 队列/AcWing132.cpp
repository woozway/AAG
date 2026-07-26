#include <bits/stdc++.h>
using namespace std;
const int N = 1010, M = 1e6 + 10;
int teamid[M]; // 存储编号为 x 的人属于哪一个队伍（队伍编号 0 ~ n-1）

int main() {
  int n, C = 1;
  while (cin >> n, n) {
    queue<int> team;
    queue<int> person[N];
    printf("Scenario #%d\n", C ++ );
    for (int i = 0; i < n; i ++ ) {
      int cnt;
      cin >> cnt;
      while (cnt -- ) {
        int x;
        cin >> x;
        teamid[x] = i;
      }
    }

    string command;
    while (cin >> command, command != "STOP")
      if (command == "ENQUEUE") {
        int x;
        cin >> x;
        int tid = teamid[x];
        if (person[tid].empty()) team.push(tid);
        person[tid].push(x);
      }
      else {
        int tid = team.front();
        auto &q = person[tid];
        cout << q.front() << endl;
        q.pop();
        if (q.empty()) team.pop();
      }

    cout << endl;
  }

  return 0;
}