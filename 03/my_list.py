class MyList(list):
    def __init__(self, input_lst=list()):
        self.__lst = input_lst

    @property
    def lst(self):
        return self.__lst


    def __eq__(self, other):
        sum_self = 0
        sum_other = 0

        for i in range(len(self)):
            sum_self += self[i]

        for j in range(len(other)):
            sum_other += other[j]

        if (sum_self == sum_other):
            return True

        return False

    @classmethod
    def __add_zeros(self, lst, num_elems):
        list_cur_size = len(lst)

        if list_cur_size < num_elems:
            list_with_zeros = lst.copy()

            for _ in range(list_cur_size, num_elems):
                list_with_zeros.append(0)

            return list_with_zeros

        return lst

    @classmethod
    def __get_max_list_by_size(self, lst1, lst2):
        lst1_size = len(lst1)
        lst2_size = len(lst2)

        if lst1_size > lst2_size:
            return lst1
        elif lst2_size > lst1_size:
            return lst2
        
        return None

    @classmethod
    def from_my_list_to_list(cls, lst1, lst2):
        if lst1.__class__ is cls:
            left = lst1.lst
        else:
            left = lst1
        
        if lst2.__class__ is cls:
            right = lst2.lst
        else:
            right = lst2
        
        return left, right

    @classmethod
    def __handle_2list(cls, left, right):

        upper_list = cls.__get_max_list_by_size(left, right)

        if upper_list is not None:
            left_size = len(left)
            right_size = len(right)
            max_size = max(left_size, right_size)

            if left_size < right_size:
                lst_with_zeros = cls.__add_zeros(left, max_size)

                return lst_with_zeros, upper_list
            else:
                lst_with_zeros = cls.__add_zeros(right, max_size)

                return upper_list, lst_with_zeros
    
        return left, right


    def __add__(self, other):
        left, right = self.__class__.from_my_list_to_list(self, other)

        left, right = self.__class__.__handle_2list(left, right)

        add_lst = self.__class__([0] * len(left))

        for i in range(len(left)):
            add_lst[i] += left[i] + right[i]
        
        return add_lst


    def __radd__(self, other):
        left, right = self.from_my_list_to_list(self, other)

        left, right = self.__class__.__handle_2list(left, right)

        add_lst = self.__class__([0] * len(left))

        for i in range(len(left)):
            add_lst[i] += left[i] + right[i]
        
        return add_lst


    def __sub__(self, other):
        left, right = self.from_my_list_to_list(self, other)

        left, right = self.__class__.__handle_2list(left, right)

        add_lst = self.__class__([0] * len(left))

        for i in range(len(left)):
            add_lst[i] += left[i] - right[i]
        
        return add_lst


    def __rsub__(self, other):
        right, left = self.from_my_list_to_list(self, other)

        left, right = self.__class__.__handle_2list(left, right)

        add_lst = self.__class__([0] * len(left))

        for i in range(len(left)):
            add_lst[i] += left[i] - right[i]
        
        return add_lst


    def __len__(self):
        return len(self.__lst);

    def __getitem__(self, key):
        return self.__lst[key]

    def __setitem__(self, key, value):
        self.__lst[key] = value


    def __str__(self):
        sum_elems = 0
        lst_size = len(self)

        res_str = "["

        if (len(self) != 0):
            res_str += str(self.__lst[0])
            sum_elems += self.__lst[0]

        for i in range(1, lst_size):
            res_str += ", " + str(self.__lst[i])
            sum_elems += self.__lst[i]

        res_str += "] " + str(sum_elems)

        return res_str


a = MyList([1, 0])
b = MyList([0, 2, -3, 4])

b_list = [0, 3, -2]

print("a?b=", [0, -1, 2] - MyList([0, 1, 3, 5]))

