import unittest
from unittest.mock import patch
from io import StringIO

from server import Server


class TestServer(unittest.TestCase):
    # divide_glued_urls
    def test_server_divide_glued_urls(self):
        with patch("sys.stdout", new=StringIO()):
            srv = Server(10, 7)
            urls = "https://123\nhttps://456\n"
            srv.divide_glued_urls(urls)

            self.assertEqual(srv._que.qsize(), 2)
            self.assertEqual(
                srv._que.get(), "https://123"
            )
            self.assertEqual(
                srv._que.get(), "https://456"
            )
