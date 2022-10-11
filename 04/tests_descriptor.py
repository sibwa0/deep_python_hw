from descriptor import Integer, PositiveInteger, String, Data

import unittest
from unittest.mock import patch
from io import StringIO

class TestDescriptor(unittest.TestCase):
    # empty init
    def test_init_data_empty(self):
        with patch('sys.stdout', new=StringIO()):
            data = Data()

            self.assertEqual(
                (data.num, data.name, data.price),
                (None, None, None)
            )

    # Integer
    def test_integer_correct(self):
        with patch('sys.stdout', new=StringIO()):
            data = Data()

            data.num = 10

            self.assertEqual(
                data.num,
                10
            )

    def test_integer_wrong(self):
        with patch('sys.stdout', new=StringIO()):
            data = Data()

            data.num = 10.5

            self.assertEqual(
                data.num,
                None
            )

    # String
    def test_string_correct(self):
        with patch('sys.stdout', new=StringIO()):
            data = Data()

            data.name = "Alexey"

            self.assertEqual(
                data.name,
                "Alexey"
            )

    def test_string_wrong(self):
        with patch('sys.stdout', new=StringIO()):
            data = Data()

            data.name = 10.5

            self.assertEqual(
                data.name,
                None
            )

    def test_positive_integer_correct(self):
        with patch('sys.stdout', new=StringIO()):
            data = Data()

            data.price = 10.5

            self.assertEqual(
                data.price,
                10.5
            )

    def test_positive_integer_wrong(self):
        with patch('sys.stdout', new=StringIO()):
            data = Data()

            data.price = -5

            self.assertEqual(
                data.price,
                None
            )
        