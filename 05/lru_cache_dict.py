class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.size = 0
        self._dct = {}

    def get(self, key):
        if key not in self._dct:
            return None

        for i in self._dct:
            if i != key:
                self._dct[i] = (self._dct[i][0], self._dct[i][1] + 1)
            else:
                self._dct[i] = (self._dct[i][0], 0)

        return self._dct[key][0]

    def set(self, key, value):
        if self.size < self.limit:
            for i in self._dct:
                self._dct[i] = (self._dct[i][0], self._dct[i][1] + 1)

            self._dct[key] = (value, 0)
            self.size += 1

        elif self.size == self.limit:
            for i in self._dct:
                self._dct[i] = (self._dct[i][0], self._dct[i][1] + 1)
                if self._dct[i][1] == self.limit:
                    edge = i

            if edge != key:
                del self._dct[edge]

            self._dct[key] = (value, 0)

    def __str__(self) -> str:
        return str(self._dct)
