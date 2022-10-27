import socket
import sys
import threading
import queue
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
# import logging
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
        # num_workers fix
        self.server.listen(num_workers)
        
        # QUUUUEEEEUUUEEE
        self._que = queue.Queue(110)#num_workers)
        # self._lock = threading.Lock()
        self._cnt = Counter()

        self._threads = [
            threading.Thread(
                target=self.handle_url,
                args=(),
                name=f"{i} Th"
            )
            for i in range(num_workers)
        ]

    def connect(self):
        while True:
            self._client, address = self.server.accept()
            print(f"Connection Established - {address[0]}:{address[1]}")

            logger_server.info("__Start Threads")
            for th in self._threads:
                th.start()

            while True:
                try:
                    logger_server.info(f"Input_ Queue size: {self._que.qsize()}")
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
            logger_server.info(f"__Handle th ::{threading.current_thread().name}::")
            try:
                wait += 1
                url = self._que.get(timeout=1)

                wait = 0
                logger_server.info(f"__Correct url: {url}")

            except Exception:
                logger_server.info(f"__Wait new url: {wait}")
                if wait == 5:
                    logger_server.info(f"__Stop th ::{threading.current_thread().name}::")
                    break
                continue

            # обработать url, записать в Counter
            html = urlopen(url).read()    
            soup = BeautifulSoup(html, 'html.parser')

            for script in soup(["script", "style"]):
                script.extract()

            text = soup.get_text()

            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    
            text = '\n'.join(chunk for chunk in chunks if chunk).split()

            # update statistic
            with threading.Lock():
                self._cnt.update(text)
                self._num_handled_urls += 1
                logger_server.info(f"Handled Amount of URLS: {self._num_handled_urls}")
                print(f"Handled Amount of URLS: {self._num_handled_urls}")

                self.handle_requests()


    def handle_requests(self):
        # for th in self._threads:
        #     th.start()
        
        # for th in self._threads:
        #     th.join()

        # logic: pack into json, send answer
        top_k_words_cnt = self._cnt.most_common(self._num_top_words)
        js = json.dumps(top_k_words_cnt, ensure_ascii=False)

        logger_server.info(f"__send Answer: {js}")
        self._client.send(bytes(js, "utf-8"))



if __name__ == "__main__":
    parser = console_server_input()
    server_input = parser.parse_args(sys.argv[1:])

    # print (f"w={namespace.k}, k={namespace.w}")

    srv = Server(server_input.w, server_input.k)
    srv.connect()
    # srv.handle_requests()


    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server.bind((IP, PORT))
    # server.listen(5)

    # while True:
    #     client, address = server.accept()
    #     print(f"Connection Established - {address[0]}:{address[1]}")

    #     string = client.recv(1024).decode("utf-8")

    #     # miss logic

    #     client.send(bytes(string, "utf-8"))
        # client.close()
