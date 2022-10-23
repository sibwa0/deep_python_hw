import unittest

from filter_file import filter_file, filter_file_gen
from lru_cache_dict import LRUCache


class TestFilterFile(unittest.TestCase):
    # func impl
    # targets are in file
    # def test_targets_in_file(self):
    #     targets = ["роза", "яяя"]
    #     self.assertEqual(
    #         filter_file("file_for_filter.txt", targets),
    #         [
    #             '    а Роза упала на лапу Азора  \n',
    #             'РОЗА\n'
    #         ]
    #     )

    # # targets arent in file
    # def test_targers_not_in_file(self):
    #     targets = ["роз", "яяя"]
    #     self.assertEqual(
    #         filter_file("file_for_filter.txt", targets),
    #         []
    #     )

    # generator impl
    # targets are in file
    def test_targets_in_file_gen(self):
        with open("file_for_filter.txt", "r", encoding='utf-8') as file_desc:
            targets = ["роза", "яяя"]
            result = []

            for sentence in filter_file_gen(file_desc, targets):
                result.append(sentence)

            self.assertEqual(
                result,
                [
                    '    а Роза упала на лапу Азора  \n',
                    'РОЗА\n'
                ]
            )

    # targets arent in file
    def test_targers_not_in_file_gen(self):
        with open("file_for_filter.txt", "r", encoding='utf-8') as file_desc:
            targets = ["роз", "яяя"]
            result = []

            for sentence in filter_file_gen(file_desc, targets):
                result.append(sentence)

            self.assertEqual(
                result,
                [
                ]
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
