import unittest

from meta import CustomClass
from descriptor import Data


class TestMeta(unittest.TestCase):
    # __setattr__
    def test_custom_setattr_magic_method(self):
        inst = CustomClass()
        self.assertEqual(inst.__setattr__("__name__", "hello"), None)

    # __getattribute__
    def test_custom_getattribute_name_in_class_wrong(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.x

    def test_custom_getattribute_name_in_class_correct(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)

    def test_custom_getattribute_add_new_attr(self):
        inst = CustomClass()
        inst.dynamic = "added later"

        with self.assertRaises(AttributeError):
            inst.dynamic

        self.assertEqual(inst.custom_dynamic, "added later")

    # line()
    def test_custom_line_correct(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_line(), 100)

    def test_custom_line_wrong(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.line()

    # str()
    def test_custom_str_correct(self):
        inst = CustomClass()
        self.assertEqual(str(inst), "Custom_by_metaclass")


class TestDescriptor(unittest.TestCase):
    # empty init
    def test_init_data_empty(self):
        data = Data()

        self.assertEqual(
            (data.num, data.name, data.price),
            (0, "", 0)
        )

    # Integer
    def test_integer_correct(self):
        data = Data()

        data.num = 10
        self.assertEqual(data.num, 10)

        data.num = 20
        self.assertEqual(data.num, 20)

    def test_integer_wrong(self):
        data = Data()

        with self.assertRaises(ValueError):
            data.num = 10.5

    # String
    def test_string_correct(self):
        data = Data()

        data.name = "Alexey"
        self.assertEqual(data.name, "Alexey")

        data.name = "Alex"
        self.assertEqual(data.name, "Alex")

    def test_string_wrong(self):
        data = Data()

        with self.assertRaises(ValueError):
            data.name = 10.5

    def test_positive_integer_correct(self):
        data = Data()

        data.price = 10.5
        self.assertEqual(data.price, 10.5)

        data.price = 15
        self.assertEqual(data.price, 15)

    def test_positive_integer_wrong(self):
        data = Data()

        with self.assertRaises(ValueError):
            data.price = -5

    # __delete__
    def test_delete(self):
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
