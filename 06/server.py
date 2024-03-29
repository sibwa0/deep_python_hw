import socket
import sys
import threading
import queue
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from utils import IP, PORT, console_server_input, setup_logger


# constants
logger_server = setup_logger('second_logger', 'server_logfile.log')


class Server:
    def __init__(self, num_workers, num_top_words):
        logger_server.info("__INIT__")
        self._num_workers = num_workers
        self._num_top_words = num_top_words
        self._num_handled_urls = 0

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((IP, PORT))
        self.server.listen(num_workers)

        self._que = queue.Queue(110)
        self._cnt = Counter()

        self._threads = [
            threading.Thread(
                target=self.handle_url,
                args=(),
                name=f"{i} Th"
            )
            for i in range(num_workers)
        ]

    def start(self):
        while True:
            self._client, address = self.server.accept()
            print(f"Connection Established - {address[0]}:{address[1]}")

            logger_server.info("__Start Threads")
            for thread in self._threads:
                thread.start()

            while True:
                try:
                    logger_server.info(
                        "Input_ Queue size: %s",
                        self._que.qsize()
                    )
                    url = self._client.recv(1024).decode("utf-8")
                except Exception:
                    continue

                # add url in queue
                self.divide_glued_urls(url)

    def divide_glued_urls(self, glued_urls: str) -> str:
        glued_urls = glued_urls.replace("\n", "")
        http_start = glued_urls.find("http")
        http_end = glued_urls[1:].find("http")

        while http_start != -1:
            if http_end == -1:
                url = glued_urls[:]
                self._que.put(url)
                break

            url = glued_urls[:http_end + 1]
            http_start = http_end + 1
            glued_urls = glued_urls[http_start:]
            http_end = glued_urls[1:].find("http")

            self._que.put(url)

    def handle_url(self):
        wait = 0
        while True:
            logger_server.info(
                "__Handle th ::%s::",
                threading.current_thread().name
            )
            try:
                wait += 1
                url = self._que.get(timeout=1)

                wait = 0
                logger_server.info("__Correct url: %s", url)

            except Exception:
                logger_server.info("__Wait new url: %s", wait)
                if wait == 5:
                    logger_server.info(
                        "__Stop th ::%s::",
                        threading.current_thread().name
                    )
                    break
                continue

            # обработать url, записать в Counter
            text = self.get_text_from_url(url)

            # update statistic
            with threading.Lock():
                self._cnt.update(text)
                self._num_handled_urls += 1
                logger_server.info(
                    "Handled Amount of URLS: %s",
                    self._num_handled_urls
                )
                print(f"Handled Amount of URLS: {self._num_handled_urls}")

                self.handle_requests()

    def get_text_from_url(self, url):
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text()

        lines = (line.strip() for line in text.splitlines())
        chunks = (
            phrase.strip() for line in lines for phrase in line.split("  ")
        )

        text = '\n'.join(chunk for chunk in chunks if chunk).split()

        return text

    def handle_requests(self):
        # logic: pack into json, send answer
        top_k_words_cnt = self._cnt.most_common(self._num_top_words)
        js_str = json.dumps(top_k_words_cnt, ensure_ascii=False)

        logger_server.info("__Send Answer: %s", js_str)
        self._client.send(bytes(js_str, "utf-8"))


if __name__ == "__main__":
    parser = console_server_input()
    server_input = parser.parse_args(sys.argv[1:])

    srv = Server(server_input.w, server_input.k)
    srv.start()
