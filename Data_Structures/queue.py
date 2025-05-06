from collections import deque

class Queue:
    """
    A queue backed by collections.deque.
    Time complexity:
      • enqueue: O(1)
      • dequeue: O(1)
    Space complexity: O(n)
    """
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.buffer.popleft()

    def is_empty(self) -> bool:
        return not self.buffer

    def size(self) -> int:
        return len(self.buffer)

    def __len__(self) -> int:
        return len(self.buffer)

    def __repr__(self):
        return f"Queue({list(self.buffer)})"