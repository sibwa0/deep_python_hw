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

        self.assertFalse(my_lst1 == my_lst2)

    # __add_zeros
    # def test_add_zeros_same_len(self):
    #     my_lst = MyList([0, 3, 2])

    #     self.assertEqual(MyList._MyList__add_zeros(my_lst.lst, 3), [0, 3, 2])

    # def test_add_zeros_dif_len(self):
    #     my_lst = MyList([0, 3, 2])

    #     self.assertEqual(
    #         MyList._MyList__add_zeros(my_lst.lst, 5), [0, 3, 2, 0, 0]
    #     )

    # # __get_max_list_by_size
    # def test___get_max_list_by_size_dif_len(self):
    #     lst1 = [0, 1, 2, 5]
    #     lst2 = [2, 3, 1]

    #     self.assertEqual(
    #         MyList._MyList__get_max_list_by_size(lst1, lst2), [0, 1, 2, 5]
    #     )

    # def test___get_max_list_by_size_same_len(self):
    #     lst1 = [0, 1, 2]
    #     lst2 = [2, 3, 1]

    #     self.assertIsNone(MyList._MyList__get_max_list_by_size(lst1, lst2))

    # # from_my_list_to_list
    # def test_from_my_list_to_list_two_my_list(self):
    #     my_lst1 = MyList([0, -1, 2])
    #     my_lst2 = MyList([0, 1, 2])

    #     self.assertEqual(
    #         MyList.from_my_list_to_list(my_lst1, my_lst2),
    #         ([0, -1, 2], [0, 1, 2])
    #     )

    # def test_from_my_list_to_list_one_my_list_left(self):
    #     my_lst = MyList([0, -1, 2])
    #     lst = [0, 1, 2]

    #     self.assertEqual(
    #         MyList.from_my_list_to_list(my_lst, lst), ([0, -1, 2], [0, 1, 2])
    #     )

    # def test_from_my_list_to_list_one_my_list_right(self):
    #     lst = [0, 1, 2]
    #     my_lst = MyList([0, -1, 2])

    #     self.assertEqual(
    #         MyList.from_my_list_to_list(lst, my_lst), ([0, 1, 2], [0, -1, 2])
    #     )

    # # __handle_2list
    # @unittest.mock.patch("my_list.MyList._MyList__get_max_list_by_size")
    # def test___handle_2list_left(self, mock_get_max_list):
    #     lst1 = [0, -1, 2, 3]
    #     lst2 = [0, 1]

    #     mock_get_max_list.return_value = [0, -1, 2, 3]

    #     self.assertEqual(
    #         MyList._MyList__handle_2list(lst1, lst2),
    #         ([0, -1, 2, 3], [0, 1, 0, 0])
    #     )

    # @unittest.mock.patch("my_list.MyList._MyList__get_max_list_by_size")
    # def test___handle_2list_right(self, mock_get_max_list):
    #     lst1 = [0, 1]
    #     lst2 = [0, -1, 2, 3]

    #     mock_get_max_list.return_value = [0, -1, 2, 3]

    #     self.assertEqual(
    #         MyList._MyList__handle_2list(lst1, lst2),
    #         ([0, 1, 0, 0], [0, -1, 2, 3])
    #     )

    # @unittest.mock.patch("my_list.MyList._MyList__get_max_list_by_size")
    # def test___handle_2list_same_len(self, mock_get_max_list):
    #     lst1 = [5, 1]
    #     lst2 = [0, -1]

    #     mock_get_max_list.return_value = None

    #     self.assertEqual(
    #         MyList._MyList__handle_2list(lst1, lst2),
    #         ([5, 1], [0, -1])
    #     )

    # __add__, __radd__
    def test__add__two_my_list(self):
        my_lst1 = MyList([0, -1, 2])
        my_lst2 = MyList([0, 1, 3])

        self.assertEqual(my_lst1 + my_lst2, MyList([0, 0, 5]))

    def test__add__one_my_list_left(self):
        my_lst = MyList([0, -1, 2])
        lst = [0, 1, 3, 5]

        self.assertEqual(my_lst + lst, MyList([0, 0, 5, 5]))

    def test__radd__one_my_list_right(self):
        lst = [0, -1, 2]
        my_lst = MyList([0, 1, 3, 5])

        self.assertEqual(lst + my_lst, MyList([0, 0, 5, 5]))

    # __sub__, __rsub__
    def test__sub__two_my_list(self):
        my_lst1 = MyList([0, -1, 2])
        my_lst2 = MyList([0, 1, 3, 5])

        self.assertEqual(my_lst1 - my_lst2, MyList([0, -2, -1, -5]))

    def test__sub__one_my_list_left(self):
        my_lst = MyList([0, -1, 2])
        lst = [0, 1, 3, 5]

        self.assertEqual(my_lst - lst, MyList([0, -2, -1, -5]))

    def test__rsub__one_my_list_right(self):
        lst = [0, -1, 2]
        my_lst = MyList([0, 1, 3, 5])

        self.assertEqual(lst - my_lst, MyList([0, -2, -1, -5]))
