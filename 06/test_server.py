import socket
import argparse
import sys
import threading
import queue
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging

from test_client import PORT, IP


# constants
logging.basicConfig(level=logging.INFO, filename="server_info.log", filemode="w")


# console input 
def console_server_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', default=0, type=int)
    parser.add_argument('-k', default=0, type=int)
 
    return parser


class Server:
    def __init__(self, num_workers, num_top_words):
        logging.info("__INIT__")
        self._num_workers = num_workers
        self._num_top_words = num_top_words
        self._num_handled_urls = 0

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((IP, PORT))
        self.server.listen(num_workers)
        
        self._que = queue.Queue(num_workers)
        self._lock = threading.Lock()
        self._cnt = Counter()

        self.threads = [
            threading.Thread(
                target=self.handle_url,
                args=(self._que, self._cnt, self._lock),
            )
            for _ in range(num_workers)
        ]

    def connect(self):
        while True:
            client, address = self.server.accept()
            print(f"Connection Established - {address[0]}:{address[1]}")

            # get URLS in loop
            url = client.recv(1024).decode("utf-8")
            self._que.put(url)

            print(url, self._que.qsize())
            logging.info(self._que.qsize())

            # miss logic

            # client.send(bytes(string, "utf-8"))
    
    def handle_url(self, que, cnt, lock):
        while True:
            logging.info("__HANDLE_URL__")
            try:
                url = que.get(timeout=1)
                if url is None:
                    break

            except Exception:
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

            lock.acquire()

            cnt.update(text)
            self._num_handled_urls += 1
            logging.info(f"Handled URLS Number: {self._num_handled_urls}")

            lock.release()

    # def realese_queue(self):




if __name__ == "__main__":
    parser = console_server_input()
    server_input = parser.parse_args(sys.argv[1:])

    # print (f"w={namespace.k}, k={namespace.w}")

    srv = Server(server_input.k, server_input.w)
    srv.connect()


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
