class Stack:
    """
    A stack using Python’s built-in list.
    Time complexity:
      • push: O(1)
      • pop: O(1)
      • peek: O(1)
    Space complexity: O(n)
    """
    def __init__(self):
        self.container = []

    def push(self, val):
        self.container.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.container.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.container[-1]

    def is_empty(self) -> bool:
        return len(self.container) == 0

    def size(self) -> int:
        return len(self.container)

    def __len__(self) -> int:
        return len(self.container)

    def __repr__(self):
        return f"Stack({self.container})"