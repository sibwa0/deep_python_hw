from collections import defaultdict


class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.size = 0
        self.def_dct = defaultdict(lambda val, size: (val, size))

    def get(self, key):
        if key not in self.def_dct:
            return None

        return self.def_dct[key][0]

    def set(self, key, value):
        if self.size < self.limit:
            self.def_dct[key] = (value, self.size)
            self.size += 1

        elif self.size == self.limit:
            for i in self.def_dct:
                if self.def_dct[i][1] == self.size - 1:
                    self.def_dct[key] = (value, self.size - 1)
                    del self.def_dct[i]
                    break

    def __str__(self) -> str:
        return str(self.def_dct)
