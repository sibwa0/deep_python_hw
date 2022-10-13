import unittest
from unittest.mock import patch
from io import StringIO

from meta import CustomClass


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
