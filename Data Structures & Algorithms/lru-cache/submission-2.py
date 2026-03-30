class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int):
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            oldestKey = next(iter(self.cache))
            del self.cache[oldestKey]
       