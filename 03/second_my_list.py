class MyList(list):
    def __init__(self, input_lst):
        for i in input_lst:
            self.append(i)

    def __lt__(self, other) -> bool:
        return sum(self) < sum(other)

    def __le__(self, other) -> bool:
        return sum(self) <= sum(other)

    def __eq__(self, other) -> bool:
        return sum(self) == sum(other)

    def __ne__(self, other) -> bool:
        return sum(self) != sum(other)

    def __gt__(self, other) -> bool:
        return sum(self) > sum(other)

    def __ge__(self, other) -> bool:
        return sum(self) >= sum(other)

    @staticmethod
    def __get_iters_large(self_list: list, other: list):
        self_size = len(self_list)
        other_size = len(other)

        iters, smaller, bigger = \
            (self_size, other, self_list) if self_size >= other_size \
            else (other_size, self_list, other)

        return iters, smaller, bigger

    def __add__(self, other) -> list:
        iters, smaller, bigger = self.__get_iters_large(self, other)

        res = MyList([])

        tmp_smaller = smaller.copy()
        for _ in range(len(smaller), iters):
            tmp_smaller.append(0)

        for i in range(iters):
            res.append(bigger[i] + tmp_smaller[i])

        return res

    def __radd__(self, other) -> list:
        iters, smaller, bigger = self.__get_iters_large(self, other)

        res = MyList([])

        tmp_smaller = smaller.copy()
        for _ in range(len(smaller), iters):
            tmp_smaller.append(0)

        for i in range(iters):
            res.append(bigger[i] + tmp_smaller[i])

        return res

    def __sub__(self, other) -> list:
        iters, smaller, bigger = self.__get_iters_large(self, other)

        res = MyList([])

        tmp_smaller = smaller.copy()
        for _ in range(len(smaller), iters):
            tmp_smaller.append(0)

        if iters == len(self):
            first, second = bigger, tmp_smaller
        else:
            first, second = tmp_smaller, bigger

        for i in range(iters):
            res.append(first[i] - second[i])

        return res

    def __rsub__(self, other) -> list:
        iters, smaller, bigger = self.__get_iters_large(self, other)

        res = MyList([])

        tmp_smaller = smaller.copy()
        for _ in range(len(smaller), iters):
            tmp_smaller.append(0)

        if iters == len(self):
            first, second = tmp_smaller, bigger
        else:
            first, second = bigger, tmp_smaller

        for i in range(iters):
            res.append(first[i] - second[i])

        return res

    def __str__(self) -> str:
        return f"{super().__str__()} {sum(self)}"


def is_same(lst1: list, lst2: list) -> bool:
    if type(lst1) != type(lst2):
        return False

    if len(lst1) != len(lst2):
        return False

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


if __name__ == "__main__":
    my_list = MyList([])
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(10)
    cmp_list = MyList([-1, 2, 3])
    # cmp_list = [-1, 2, 3]

    print(f"my_list =\t{my_list}")
    print(f"cmp_list =\t{cmp_list}", end="\n\n")

    print(f"list + cmp =\t{my_list + cmp_list}", end="\n\n")
    print(f"cmp + list =\t{cmp_list + my_list}", end="\n\n")
    print(f"list - cmp =\t{my_list - cmp_list}", end="\n\n")
    print(f"cmp - list =\t{cmp_list - my_list}", end="\n\n")
