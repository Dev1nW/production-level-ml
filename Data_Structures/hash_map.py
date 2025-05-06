class HashTable:
    """
    A hash table using separate chaining.
    Time complexity:
      • insert/lookup/delete: average O(1), worst-case O(n) (all keys collide)
    Space complexity: O(n + b) where b = number of buckets.
    """
    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        # each bucket is a list of (key, value) pairs
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.capacity

    def __setitem__(self, key: str, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def __getitem__(self, key: str):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def __delitem__(self, key: str):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found")

    def get(self, key: str, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key: str) -> bool:
        idx = self._hash(key)
        return any(k == key for k, _ in self.buckets[idx])