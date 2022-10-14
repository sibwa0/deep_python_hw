from collections import defaultdict
# my_deque = deque([], maxlen=2)

# my_deque.appendleft(("k1", "val1"))

# my_deque.appendleft(("k2", "val2"))
# print(my_deque)


# my_deque.append(("k3", "val3"))
# # print(my_deque[2])
# print(my_deque)

# lst = [1, 2, 3, 4, 5]
# print(lst.pop())
# print(lst)
_size=0
dd = defaultdict(lambda val, size: (val, size))
dd[1] = (5, 3)
dd[5] = (4, _size)
print(dd)