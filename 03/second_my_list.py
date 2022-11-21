class MyList(list):
    def __init__(self, input_lst):
        for i in range(len(input_lst)):
            self.append(input_lst[i])

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
    def __get_iters_large(self: list, other: list):
        self_size = len(self)
        other_size = len(other)

        iters, bigger = (other_size, self) if self_size >= other_size else (self_size, other)

        return iters, bigger

    def __add__(self, other) -> list:
        iters, bigger = self.__get_iters_large(self, other)

        res = MyList([])

        for i in range(iters):
            res.append(self[i] + other[i])
        for j in range(iters, len(bigger)):
            res.append(bigger[j])
        
        return res

    def __radd__(self, other) -> list:
        iters, bigger = self.__get_iters_large(self, other)

        res = MyList([])

        for i in range(iters):
            res.append(self[i] + other[i])
        for j in range(iters, len(bigger)):
            res.append(bigger[j])
        
        return res
    
    def __sub__(self, other) -> list:
        iters, bigger = self.__get_iters_large(self, other)

        res = MyList([])

        for i in range(iters):
            res.append(self[i] - other[i])

        reverse = 1
        if bigger is other:
            reverse = -1

        for j in range(iters, len(bigger)):
            res.append(reverse * bigger[j])
        
        return res
    
    def __rsub__(self, other) -> list:
        iters, bigger = self.__get_iters_large(self, other)

        res = MyList([])

        reverse = -1
        if bigger is other:
            reverse = 1
        
        for i in range(iters):
            res.append(other[i] - self[i])
        for j in range(iters, len(bigger)):
            res.append(reverse * bigger[j])
        
        return res

    def __str__(self) -> str:
        return f"{super().__str__()} {sum(self)}"

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