import unittest
from server import Server


class TestServer(unittest.TestCase):
    # divide_glued_urls
    def test_server_divide_glued_urls(self):
        srv = Server(10, 7)
        urls = "https://123\nhttps://456\nhttps://789"
        srv.divide_glued_urls(urls)

        self.assertEqual(srv._que.qsize(), 3)
        self.assertEqual(
            (srv._que.get(), "https://123"),
            (srv._que.get(), "https://456"),
            (srv._que.get(), "https://789")
        )