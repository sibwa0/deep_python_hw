from meta import CustomClass, CustomMeta

import unittest
from unittest.mock import patch
from io import StringIO

class TestMeta(unittest.TestCase):
    # init CustomClass object
    # self.inst = CustomClass()
    def init_custom_class(self):
        with patch('sys.stdout', new=StringIO()):
            self.inst = CustomClass()

    # __setattr__
    def test_custom_setattr_magic_method(self):
        with patch('sys.stdout', new=StringIO()):
            self.inst = CustomClass()
            self.assertEqual(self.inst.__setattr__("__init__", "hello"), None)

    def test_custom_setattr_desired_name(self):
        with patch('sys.stdout', new=StringIO()):
            inst = CustomClass()
            self.assertEqual(inst.__setattr__("test_attr", "hello"), None)

    # __getattribute__
    def test_custom_getattribute_name_in_class_wrong(self):
        with patch('sys.stdout', new=StringIO()):
            inst = CustomClass()
            self.assertEqual(inst.x, AttributeError)

    def test_custom_getattribute_name_in_class_correct(self):
        with patch('sys.stdout', new=StringIO()):
            inst = CustomClass()
            self.assertEqual(inst.__getattribute__("custom_x"), CustomClass.custom_x)

    # line()
    def test_custom_line_correct(self):
        with patch('sys.stdout', new=StringIO()):
            inst = CustomClass()
            self.assertEqual(inst.custom_line(), 100)
    
    def test_custom_line_wrong(self):
        with patch('sys.stdout', new=StringIO()):
            inst = CustomClass()
            self.assertEqual(inst.line(), AttributeError)

    # str()
    def test_custom_str_correct(self):
        with patch('sys.stdout', new=StringIO()):
            inst = CustomClass()
            self.assertEqual(str(inst), "Custom_by_metaclass")
