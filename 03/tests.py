import unittest
import unittest.mock

from my_list import MyList

class TestMyList(unittest.TestCase):

    def test_set_up(self):
        self.my_list = MyList()

    # __len__
    def test_print_object(self):
        my_list = MyList([0, -1, 2])
        self.assertEqual(MyList.__str__(my_list), "[0, -1, 2] 1")

    # __eq__
    def test_eq_same_objects(self):
        a = MyList([0, -1, 2])
        b = MyList([0, -1, 2])

        self.assertTrue(a == b)
    
    def test_eq_equal_sum(self):
        a = MyList([0, 5, 2])
        b = MyList([3, 0, 4])

        self.assertTrue(a == b)

    def test_eq_dif_objects(self):
        a = MyList([0, -1, 2])
        b = MyList([0, 1, 2])

        self.assertFalse(a == b)

    # __add_zeros
    def test_add_zeros_same_len(self):
        a = MyList([0, 3, 2])
        
        self.assertEqual(MyList._MyList__add_zeros(a.lst, 3), [0, 3, 2])

    def test_add_zeros_dif_len(self):
        a = MyList([0, 3, 2])
        
        self.assertEqual(MyList._MyList__add_zeros(a.lst, 5), [0, 3, 2, 0, 0])

    # __get_max_list_by_size
    def test___get_max_list_by_size_dif_len(self):
        lst1 = [0, 1, 2, 5]
        lst2 = [2, 3, 1]

        self.assertEqual(MyList._MyList__get_max_list_by_size(lst1, lst2), [0, 1, 2, 5])
    
    def test___get_max_list_by_size_same_len(self):
        lst1 = [0, 1, 2]
        lst2 = [2, 3, 1]

        self.assertIsNone(MyList._MyList__get_max_list_by_size(lst1, lst2))

    # from_my_list_to_list
    def test_from_my_list_to_list_2MyList(self):
        a = MyList([0, -1, 2])
        b = MyList([0, 1, 2])

        self.assertEqual(MyList.from_my_list_to_list(a, b), ([0, -1, 2], [0, 1, 2]))

    def test_from_my_list_to_list_1MyList_left(self):
        a = MyList([0, -1, 2])
        b = [0, 1, 2]

        self.assertEqual(MyList.from_my_list_to_list(a, b), ([0, -1, 2], [0, 1, 2]))

    def test_from_my_list_to_list_1MyList_right(self):
        a = [0, 1, 2]
        b = MyList([0, -1, 2])

        self.assertEqual(MyList.from_my_list_to_list(a, b), ([0, 1, 2], [0, -1, 2]))

    # __handle_2list
    @unittest.mock.patch("my_list.MyList._MyList__get_max_list_by_size")
    def test___handle_2list_left(self, mock_get_max_list):
        a = [0, -1, 2, 3]
        b = [0, 1]

        mock_get_max_list.return_value = [0, -1, 2, 3]

        self.assertEqual(MyList._MyList__handle_2list(a, b), ([0, -1, 2, 3], [0, 1, 0, 0]))

    @unittest.mock.patch("my_list.MyList._MyList__get_max_list_by_size")
    def test___handle_2list_right(self, mock_get_max_list):
        a = [0, 1]
        b = [0, -1, 2, 3]

        mock_get_max_list.return_value = [0, -1, 2, 3]

        self.assertEqual(MyList._MyList__handle_2list(a, b), ([0, 1, 0, 0], [0, -1, 2, 3]))

    @unittest.mock.patch("my_list.MyList._MyList__get_max_list_by_size")
    def test___handle_2list_right(self, mock_get_max_list):
        a = [5, 1]
        b = [0, -1]

        mock_get_max_list.return_value = None

        self.assertEqual(MyList._MyList__handle_2list(a, b), ([5, 1], [0, -1]))

    # __add__
    # @unittest.mock.patch("my_list.MyList.from_my_list_to_list")
    # @unittest.mock.patch("my_list.MyList._MyList__handle_2list")
    def test__add__2MyList(self):#, mock_to_list, mock_handle):
        a = MyList([0, -1, 2])
        b = MyList([0, 1, 3])

        # mock_to_list.return_value = ([0, -1, 2], [0, 1, 3])
        # mock_handle.return_value = ([0, -1, 2], [0, 1, 3])

        self.assertEqual(a + b, MyList([0, 0, 5]))

    # @unittest.mock.patch("my_list.MyList.from_my_list_to_list")
    # @unittest.mock.patch("my_list.MyList._MyList__handle_2list")
    def test__add__1MyList_left(self):#, mock_to_list, mock_handle):
        a = MyList([0, -1, 2])
        b = [0, 1, 3, 5]

        # mock_to_list.return_value = ([0, -1, 2], [0, 1, 3])
        # mock_handle.return_value = ([0, -1, 2], [0, 1, 3])

        self.assertEqual(a + b, MyList([0, 0, 5, 5]))

    # @unittest.mock.patch("my_list.MyList.from_my_list_to_list")
    # @unittest.mock.patch("my_list.MyList._MyList__handle_2list")
    def test__radd__1MyList_right(self):#, mock_to_list, mock_handle):
        a = [0, -1, 2]
        b = MyList([0, 1, 3, 5])

        # mock_to_list.return_value = ([0, -1, 2], [0, 1, 3])
        # mock_handle.return_value = ([0, -1, 2], [0, 1, 3])

        self.assertEqual(a + b, MyList([0, 0, 5, 5]))

    # __sub__
    # @unittest.mock.patch("my_list.MyList.from_my_list_to_list")
    # @unittest.mock.patch("my_list.MyList._MyList__handle_2list")
    def test__sub__2MyList(self):#, mock_to_list, mock_handle):
        a = MyList([0, -1, 2])
        b = MyList([0, 1, 3, 5])

        # mock_to_list.return_value = ([0, -1, 2], [0, 1, 3])
        # mock_handle.return_value = ([0, -1, 2], [0, 1, 3])

        self.assertEqual(a - b, MyList([0, -2, -1, -5]))

    # @unittest.mock.patch("my_list.MyList.from_my_list_to_list")
    # @unittest.mock.patch("my_list.MyList._MyList__handle_2list")
    def test__sub__1MyList_left(self):#, mock_to_list, mock_handle):
        a = MyList([0, -1, 2])
        b = [0, 1, 3, 5]

        # mock_to_list.return_value = ([0, -1, 2], [0, 1, 3])
        # mock_handle.return_value = ([0, -1, 2], [0, 1, 3])

        self.assertEqual(a - b, MyList([0, -2, -1, -5]))

    @unittest.mock.patch("my_list.MyList.from_my_list_to_list")
    @unittest.mock.patch("my_list.MyList._MyList__handle_2list")
    def test__rsub__1MyList_right(self, mock_to_list, mock_handle):
        a = [0, -1, 2]
        b = MyList([0, 1, 3, 5])

        mock_to_list.return_value = ([0, 1, 3, 5], [0, -1, 2])
        mock_handle.return_value = ([0, -1, 2, 0], [0, 1, 3, 5])

        self.assertEqual(a - b, MyList([0, -2, -1, -5]))
    