from collections import defaultdict
import unittest
from unittest.mock import patch
from io import StringIO

from filter_file import filter_file
from lru_cache_dict import LRUCache


class TestFilterFile(unittest.TestCase):
    # targets are in file
    def test_targets_in_file(self):
        targets = ["роза", "яяя"]
        self.assertEqual(
            filter_file("file_for_filter.txt", targets),
            [
                '    а Роза упала на лапу Азора  \n',
                'РОЗА\n'
            ]
        )

    # targets arent in file
    def test_targers_not_in_file(self):
        targets = ["роз", "яяя"]
        self.assertEqual(
            filter_file("file_for_filter.txt", targets),
            []
        )


class TestLRUCache(unittest.TestCase):
    def test_get_key_in(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(
            cache.get("k2"),
            "val2"
        )

    def test_get_key_not_in(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(
            cache.get("k3"),
            None
        )

    def test_get_key_rewrite(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        cache.set("k3", "val3")

        self.assertEqual(
            cache.get("k2"),
            None
        )

        self.assertEqual(
            cache.get("k3"),
            "val3"
        )