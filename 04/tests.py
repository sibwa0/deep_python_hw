import unittest
from unittest.mock import patch
from io import StringIO

from meta import CustomClass
from descriptor import Data


class TestMeta(unittest.TestCase):
    # __setattr__
    def test_custom_setattr_magic_method(self):
        with patch("sys.stdout", new=StringIO()):
            inst = CustomClass()
            self.assertEqual(inst.__setattr__("__name__", "hello"), None)

    # __getattribute__
    def test_custom_getattribute_name_in_class_wrong(self):
        with patch("sys.stdout", new=StringIO()):
            inst = CustomClass()
            with self.assertRaises(AttributeError):
                inst.x

    def test_custom_getattribute_name_in_class_correct(self):
        with patch("sys.stdout", new=StringIO()):
            inst = CustomClass()
            self.assertEqual(inst.custom_x, 50)

    def test_custom_getattribute_add_new_attr(self):
        with patch("sys.stdout", new=StringIO()):
            inst = CustomClass()
            inst.dynamic = "added later"

            with self.assertRaises(AttributeError):
                inst.dynamic

            self.assertEqual(inst.custom_dynamic, "added later")

    # line()
    def test_custom_line_correct(self):
        with patch("sys.stdout", new=StringIO()):
            inst = CustomClass()
            self.assertEqual(inst.custom_line(), 100)

    def test_custom_line_wrong(self):
        with patch("sys.stdout", new=StringIO()):
            inst = CustomClass()
            with self.assertRaises(AttributeError):
                inst.line()

    # str()
    def test_custom_str_correct(self):
        with patch("sys.stdout", new=StringIO()):
            inst = CustomClass()
            self.assertEqual(str(inst), "Custom_by_metaclass")


class TestDescriptor(unittest.TestCase):
    # empty init
    def test_init_data_empty(self):
        with patch("sys.stdout", new=StringIO()):
            data = Data()

            self.assertEqual(
                (data.num, data.name, data.price),
                (None, None, None)
            )

    # Integer
    def test_integer_correct(self):
        with patch("sys.stdout", new=StringIO()):
            data = Data()

            data.num = 10

            self.assertEqual(data.num, 10)

    def test_integer_wrong(self):
        with patch("sys.stdout", new=StringIO()):
            data = Data()

            data.num = 10.5

            self.assertEqual(data.num, None)

    # String
    def test_string_correct(self):
        with patch("sys.stdout", new=StringIO()):
            data = Data()

            data.name = "Alexey"

            self.assertEqual(data.name, "Alexey")

    def test_string_wrong(self):
        with patch("sys.stdout", new=StringIO()):
            data = Data()

            data.name = 10.5

            self.assertEqual(data.name, None)

    def test_positive_integer_correct(self):
        with patch("sys.stdout", new=StringIO()):
            data = Data()

            data.price = 10.5

            self.assertEqual(data.price, 10.5)

    def test_positive_integer_wrong(self):
        with patch("sys.stdout", new=StringIO()):
            data = Data()

            data.price = -5

            self.assertEqual(data.price, None)

    # __delete__
    def test_delete(self):
        with patch("sys.stdout", new=StringIO()):
            data = Data()

            del data.num
            del data.name
            del data.price

            with self.assertRaises(AttributeError):
                data.num

            with self.assertRaises(AttributeError):
                data.name

            with self.assertRaises(AttributeError):
                data.price
