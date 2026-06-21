#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
int n, root;
// p：父节点的编号；s：当前这个“等效节点”包含了几个原始节点；
// v：当前这个“等效节点”包含的所有原始节点的权值总和；avg：平均权值 = v / s，贪心的核心依据
struct Node {
  int p, s, v;
  double avg;
} nodes[N];

int find() { // 寻找当前树中（除根节点外）平均权值 (avg) 最大的节点
  double avg = 0;
  int res = -1;
  for (int i = 1; i <= n; i ++ )
    if (i != root && nodes[i].avg > avg) {
      avg = nodes[i].avg;
      res = i;
    }
  return res;
}

// 先算基础，再算相对延误，以避开复杂的全排序列计算
int main() {
  cin >> n >> root;
  int ans = 0;
  for (int i = 1; i <= n; i ++ ) {
    cin >> nodes[i].v;
    nodes[i].avg = nodes[i].v;
    nodes[i].s = 1;
    // 假设所有节点都在第 1 个时刻被染色，那么基础代价就是所有节点的权值之和
    // 后续如果某个节点被推迟了，我们只需要加上“推迟的时间差 * 该节点的权值”即可
    ans += nodes[i].v;
  }
  for (int i = 0; i < n - 1; i ++ ) {
    int a, b;
    cin >> a >> b;
    nodes[b].p = a;
  }

  // 贪心合并，总共需要合并 n - 1 次（把所有非根节点最终都合并到根节点上）
  for (int i = 0; i < n - 1; i ++ ) {
    int p = find();
    int father = nodes[p].p;
    // 根据贪心策略，一旦 father 被染色，我们应该【立刻】染 p
    // 这意味着，p 里面包含的节点，其实际染色时间，等于 father 里面包含的节点全部染完后的时间
    // 换句话说，p 里面的所有节点，被 father 里面的节点“向后排挤”了 father.s 个时间单位
    // 增加的代价 = 延迟的时间 (father.s) * 被延迟的权值和 (nodes[p].v)
    ans += nodes[p].v * nodes[father].s;
    nodes[p].avg = -1; // p 已经被合并了，把它的 avg 设为 -1，防止以后再被 find() 找到

    // 将 p 的所有子节点重新认 father 为新的父节点 (相当于把 p 从树中压扁了)
    for (int j = 1; j <= n; j ++ )
      if (nodes[j].p == p)
        nodes[j].p = father;
    // 更新父节点 father 的状态 (把 p 融进 father 里)
    nodes[father].v += nodes[p].v;
    nodes[father].s += nodes[p].s;
    nodes[father].avg = (double)nodes[father].v / nodes[father].s;
  }

  cout << ans << endl;
  return 0;
}