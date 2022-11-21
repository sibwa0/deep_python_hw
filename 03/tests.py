import unittest
import unittest.mock

# from my_list import MyList
from second_my_list import MyList


class TestMyList(unittest.TestCase):

    # __len__
    def test_print_object(self):
        my_list = MyList([0, -1, 2])
        self.assertEqual(MyList.__str__(my_list), "[0, -1, 2] 1")

    # __eq__
    def test_eq_same_objects(self):
        my_lst1 = MyList([0, -1, 2])
        my_lst2 = MyList([0, -1, 2])

        self.assertTrue(my_lst1 == my_lst2)

    def test_eq_equal_sum(self):
        my_lst1 = MyList([0, 5, 2])
        my_lst2 = MyList([3, 0, 4])

        self.assertTrue(my_lst1 == my_lst2)

    def test_eq_dif_objects(self):
        my_lst1 = MyList([0, -1, 2])
        my_lst2 = MyList([0, 1, 2])

        self.assertTrue(my_lst1 != my_lst2)
    
    # __lt__
    def test_lt_dif_sum(self):
        my_lst1 = MyList([0, 1, 2])
        my_lst2 = MyList([0, 10, 2])

        self.assertTrue(my_lst1 < my_lst2)

    def test_lt_same_sum(self):
        my_lst1 = MyList([5, 5, 2])
        my_lst2 = MyList([0, 10, 2])

        self.assertFalse(my_lst1 < my_lst2)

    # __le__
    def test_le_same_sum(self):
        my_lst1 = MyList([0, 1, 2])
        my_lst2 = MyList([1, 0, 2])

        self.assertTrue(my_lst1 <= my_lst2)

    def test_le_dif_sum(self):
        my_lst1 = MyList([0, 0, 2])
        my_lst2 = MyList([0, 10, 2])

        self.assertTrue(my_lst1 <= my_lst2)

    # __gt__
    def test_gt_same_sum(self):
        my_lst1 = MyList([0, 1, 2])
        my_lst2 = MyList([1, 0, 2])

        self.assertFalse(my_lst1 > my_lst2)

    def test_gt_dif_sum(self):
        my_lst1 = MyList([0, 10, 2])
        my_lst2 = MyList([0, 0, 2])

        self.assertTrue(my_lst1 > my_lst2)

    # __ge__
    def test_ge_same_sum(self):
        my_lst1 = MyList([0, 1, 2])
        my_lst2 = MyList([1, 0, 2])

        self.assertTrue(my_lst1 >= my_lst2)

    def test_ge_dif_sum(self):
        my_lst1 = MyList([0, 10, 2])
        my_lst2 = MyList([0, 0, 2])

        self.assertTrue(my_lst1 >= my_lst2)

    # __add__, __radd__
    def test__add__two_my_list_first(self):
        my_lst1 = MyList([0, -1, 2, 5])
        my_lst2 = MyList([0, 1, 3])

        self.assertEqual(my_lst1 + my_lst2, MyList([0, 0, 5, 5]))
        self.assertEqual(my_lst1, MyList([0, -1, 2, 5]))
        self.assertEqual(my_lst2, MyList([0, 1, 3]))
    
    def test__add__two_my_list_second(self):
        my_lst1 = MyList([0, -1, 2, 5])
        my_lst2 = MyList([0, 1, 3, 5, 6])

        self.assertEqual(my_lst1 + my_lst2, MyList([0, 0, 5, 10, 6]))
        self.assertEqual(my_lst1, MyList([0, -1, 2, 5]))
        self.assertEqual(my_lst2, MyList([0, 1, 3, 5, 6]))

    def test__add__one_my_list_left_second(self):
        my_lst = MyList([0, -1, 2])
        lst = [0, 1, 3, 5]

        self.assertEqual(my_lst + lst, MyList([0, 0, 5, 5]))
        self.assertEqual(my_lst, MyList([0, -1, 2]))
        self.assertEqual(lst, [0, 1, 3, 5])
    
    def test__add__one_my_list_left_first(self):
        my_lst = MyList([0, -1, 2, 5, 6])
        lst = [0, 1, 3, 5]

        self.assertEqual(my_lst + lst, MyList([0, 0, 5, 10, 6]))
        self.assertEqual(my_lst, MyList([0, -1, 2, 5, 6]))
        self.assertEqual(lst, [0, 1, 3, 5])

    def test__radd__one_my_list_right_second(self):
        lst = [0, -1, 2]
        my_lst = MyList([0, 1, 3, 5])

        self.assertEqual(lst + my_lst, MyList([0, 0, 5, 5]))
        self.assertEqual(lst, [0, -1, 2])
        self.assertEqual(my_lst, MyList([0, 1, 3, 5]))

    def test__radd__one_my_list_right_first(self):
        lst = [0, -1, 2, 5, 6]
        my_lst = MyList([0, 1, 3, 5])

        self.assertEqual(lst + my_lst, MyList([0, 0, 5, 10, 6]))
        self.assertEqual(lst, [0, -1, 2, 5, 6])
        self.assertEqual(my_lst, MyList([0, 1, 3, 5]))


    # __sub__, __rsub__
    def test__sub__two_my_list_second(self):
        my_lst1 = MyList([0, -1, 2])
        my_lst2 = MyList([0, 1, 3, 5])

        self.assertEqual(my_lst1 - my_lst2, MyList([0, -2, -1, -5]))
        self.assertEqual(my_lst1, MyList([0, -1, 2]))
        self.assertEqual(my_lst2, MyList([0, 1, 3, 5]))

    def test__sub__two_my_list_first(self):
        my_lst1 = MyList([0, -1, 2])
        my_lst2 = MyList([0, 1])

        self.assertEqual(my_lst1 - my_lst2, MyList([0, -2, 2]))
        self.assertEqual(my_lst1, MyList([0, -1, 2]))
        self.assertEqual(my_lst2, MyList([0, 1]))

    def test__sub__one_my_list_left_second(self):
        my_lst = MyList([0, -1, 2])
        lst = [0, 1, 3, 5]

        self.assertEqual(my_lst - lst, MyList([0, -2, -1, -5]))
        self.assertEqual(my_lst, MyList([0, -1, 2]))
        self.assertEqual(lst, [0, 1, 3, 5])
    
    def test__sub__one_my_list_left_first(self):
        my_lst = MyList([0, -1, 2, 5, 6])
        lst = [0, 1, 3, 5]

        self.assertEqual(my_lst - lst, MyList([0, -2, -1, 0, 6]))
        self.assertEqual(my_lst, MyList([0, -1, 2, 5, 6]))
        self.assertEqual(lst, [0, 1, 3, 5])

    def test__rsub__one_my_list_right_second(self):
        lst = [0, -1, 2]
        my_lst = MyList([0, 1, 3, 5])

        self.assertEqual(lst - my_lst, MyList([0, -2, -1, -5]))
        self.assertEqual(lst, [0, -1, 2])
        self.assertEqual(my_lst, MyList([0, 1, 3, 5]))
    
    def test__rsub__one_my_list_right_first(self):
        lst = [0, -1, 2, 5, 6]
        my_lst = MyList([0, 1, 3, 5])

        self.assertEqual(lst - my_lst, MyList([0, -2, -1, 0, 6]))
        self.assertEqual(lst, [0, -1, 2, 5, 6])
        self.assertEqual(my_lst, MyList([0, 1, 3, 5]))
