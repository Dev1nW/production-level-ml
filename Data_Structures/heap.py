class MinHeap:
    """
    A min-heap with array backing.
    Time complexity:
      • push: O(log n)
      • pop: O(log n)
      • peek: O(1)
    Space complexity: O(n)
    """
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def push(self, val):
        self.heap.append(val)
        self._up(len(self.heap) - 1)

    def _up(self, idx):
        while idx > 0 and self.heap[self._parent(idx)] > self.heap[idx]:
            p = self._parent(idx)
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            idx = p

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._down(0)
        return root

    def _down(self, idx):
        smallest = idx
        l, r = self._left(idx), self._right(idx)
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._down(smallest)

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return not self.heap

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return f"MinHeap({self.heap})"