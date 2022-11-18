import unittest
from unittest.mock import patch

import asyncio
import time
from io import StringIO
from collections import Counter
from urllib.request import urlopen

from async_handle_urls import (
    parse_encode_html,
    batch_fetch,
)


class TestAsyncHandleUrls(unittest.TestCase):
    def test_batch_fetch(self):
        with patch("sys.stdout", new=StringIO()):

            st_time = time.time()
            cnt_dct = asyncio.run(batch_fetch(1, "urls_copy.txt"))
            end_time = time.time()

            self.assertTrue(isinstance(cnt_dct, Counter))
            self.assertTrue(len(cnt_dct) > 100)
            self.assertTrue(cnt_dct.most_common(1)[0][0] == "the")
            self.assertTrue((end_time - st_time) < 5)

    def test_parse_encode_html(self):
        with open("urls_copy.txt", "r", encoding="utf-8") as urls:
            url = urls.readline()
            html = urlopen(url).read()

            text = parse_encode_html(html)

            self.assertTrue(isinstance(text, list))
            self.assertTrue(len(text) > 5)
            self.assertTrue("the" in text)
