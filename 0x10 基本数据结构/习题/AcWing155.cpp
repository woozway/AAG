#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;
int n;
queue<PII> waits; // 内存不足时，请求进入等待队列排队, <需要的内存长度 m，占用时间 p>
set<PII> runs; // 维护当前被占用的内存块，<内存块的起始下标，内存块的长度>
// 维护正在运行的任务何时结束，按结束时间从小到大，<内存释放时间点，要释放内存块的起始下标>
priority_queue<PII, vector<PII>, greater<PII>> endts;
int tm_, cnt;

// 尝试分配内存函数，t: 当前时间, m: 需要的内存长度, p: 占用时间
bool give(int t, int m, int p) {
  // 遍历当前已分配的内存块，寻找相邻内存块之间的空隙（First Fit 算法）
  for (auto it = runs.begin(); it != runs.end(); it ++ ) {
    auto jt = it;
    jt ++ ; // jt 指向 it 的下一个内存块
    if (jt != runs.end())
      // it 的结束地址为 it->first + it->second - 1；jt 的起始地址为 jt->first
      if (m <= (jt->first - 1) - (it->first + it->second) + 1) {
        // 找到了足够大的空隙，紧贴着前一个内存块 it 的尾部进行分配
        int start = it->first + it->second;
        runs.insert({start, m}); // 将新分配的内存块加入 runs 集合
        endts.push({t + p, start}); // 将该内存块的释放事件压入小根堆，释放时间为 t + p
        return true;
      }
  }
  return false;
}

// 时间推进与内存释放：推进系统时间至 t，并处理所有在 t 时刻及之前结束的任务
void finish(int t) {
  // 只要还有未完成的任务，且最早结束的任务的时间 <= 当前时间 t
  while (endts.size() && endts.top().first <= t) {
    int f = endts.top().first;
    // 同一时刻 f 可能有多个任务同时结束，把释放的所有内存全回收完毕后再去检查等待队列
    while (endts.size() && endts.top().first == f) {
      auto top = endts.top();
      endts.pop();
      // 在 runs 集合中找到对应的内存块并删除它，释放内存
      auto it = runs.lower_bound({top.second, 0});
      runs.erase(it);
    }

    tm_ = f; // 更新最后一个任务完成的时间
    while (waits.size()) { // 内存释放完毕，检查等待队列中是否有任务可以被满足
      auto front = waits.front();
      if (give(f, front.first, front.second)) waits.pop();
      else break;
    }
  }
}

int main() {
  cin >> n;
  int t, m, p;

  // 哨兵：地址两端放置两个永不释放的“虚拟内存块”
  runs.insert({-1, 1}), runs.insert({n, 1});
  while (cin >> t >> m >> p, t || m || p) {
    finish(t);
    if (!give(t, m, p)) {
      waits.push({m, p}); // 分配失败，加入等待队列并计数
      cnt ++ ;
    }
  }
  finish(2e9); // 强制执行完堆和队列中的所有剩余任务

  cout << tm_ << endl << cnt << endl;

  return 0;
}