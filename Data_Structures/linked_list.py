class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    A basic singly-linked list.
    Time complexity:
      • insert_at_head: O(1)
      • insert_at_tail: O(n)
      • search: O(n)
      • delete: O(n)
    Space complexity: O(n)
    """
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete(self, data) -> bool:
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def to_list(self) -> list:
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result