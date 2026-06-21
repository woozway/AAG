// 二叉堆，下标从1开始
int heap[SIZE], n;
void up(int p) { // 向上调整
  while (p > 1) {
    if (heap[p] > heap[p / 2]) { // 子节点>父节点，不满足大根堆性质
      swap(heap[p], heap[p / 2]);
      p /= 2;
    }
    else break;
  }	
}
// 新节点放在二叉堆数组末尾，通过交换向上调整
void Insert(int val) {
  heap[ ++ n] = val;
  up(n);
}

int GetTop() {
  return heap[1];
}

void down(int p) {
  int s = p * 2; // p的左子节点
  while (s <= n) {
    if (s < n && heap[s] < heap[s + 1]) s ++ ; // 左右子节点取较大者
    if (heap[s] > heap[p]) { // 子节点大于父节点，不满足大根堆性质
      swap(heap[s], heap[p]);
      p = s, s = p * 2;
    }
    else break;
  }
}
// 把堆顶heap[1]与末尾节点交换，然后移除末尾节点；向下调整
void Extract() {
  heap[1] = heap[n -- ];
  down(1);
}
// 删除数组下标k位置的节点时，交换heap[k]和heap[n]后可能需要向上/下调整，分别检查
void Remove(int k) {
  heap[k] = heap[n -- ];
  up(k), down(k);
}