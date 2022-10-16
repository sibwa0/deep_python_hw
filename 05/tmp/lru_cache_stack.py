class LRUCache():

        def __init__(self, limit=5):
            self.limit = limit
            self.lst = [None] * limit
            self.size = 0

        def get(self, key):
            for i in range(self.size):
                if self.lst[i][0] == key:
                    return self.lst[i][1]

            return None

        def set(self, key, value):
            if self.size < self.limit:
                self.lst[self.size] = (key, value)
                self.size += 1
            
            elif self.size == self.limit:
                self.lst[self.size - 1] = (key, value)

        def pop(self):
            self.size -= 1

        def __str__(self):
            return f"{self.lst[:self.size]} limit={self.limit}"


if __name__ == "__main__":
    cache = LRUCache(2)
    print(cache)

    cache.set("k1", "v1")
    cache.set("k2", "v2")
    print(cache, end="\n\n")

    cache.set("k3", "v3")
    cache.set("k4", "v4")
    print(cache, end="\n\n")

    cache.pop()
    print(cache.get("k4"))
    print(cache, end="\n\n")
    # print(cache.pop())

    # print(cache.get("k3"))  # None
    # print(cache.get("k2"))  # "val2"
    # print(cache.get("k1"))  # "val1"

    # cache.set("k3", "val3")

    # print(cache.get("k3"))  # "val3"
    # print(cache.get("k2"))  # None
    # print(cache.get("k1"))  # "val1"


    # Если удобнее, get/set можно сделать по аналогии с dict:
    # cache["k1"] = "val1"
    # print(cache["k3"])
