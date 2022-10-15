from collections import defaultdict

class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.size = 0
        self.dd = defaultdict(lambda val, size: (val, size))

    def get(self, key):
        if key not in self.dd:
            return None
        
        return self.dd[key][0]

    def set(self, key, value):
        if self.size < self.limit:
            self.dd[key] = (value, self.size)
            self.size += 1

        elif self.size == self.limit:
            for i in self.dd:
                if self.dd[i][1] == self.size - 1:
                    self.dd[key] = (value, self.size - 1)
                    del self.dd[i]
                    break

    def __str__(self) -> str:
        return str(self.dd)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    print(cache)

    print(cache.get("k3"))  # None
    print(cache.get("k2"))  # "val2"
    print(cache.get("k1"))  # "val1"

    cache.set("k3", "val3")

    print(cache)

    print(cache.get("k3"))  # "val3"
    print(cache.get("k2"))  # None
    print(cache.get("k1"))  # "val1"