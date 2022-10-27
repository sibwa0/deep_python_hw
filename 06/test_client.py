import socket
import sys
import threading
from itertools import islice
import time

from utils import TOP100_URL, setup_logger
from utils import IP, PORT, console_client_input, create_urls

# constants
logger_client = setup_logger('first_logger', 'client_logfile.log')


class Client:
    def __init__(self, urls_file, num_threads) -> None:
        logger_client.info("__INIT__")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((IP, PORT))

        self._urls_file = urls_file
        # self._size_urls = size_urls
        self._num_threads = num_threads

        self.threads = [
            threading.Thread(
                target=self.handle_request,
                args=(i,),
                name=f"{i} Th"
            )
            for i in range(self._num_threads)
        ]
    

    def handle_request(self, th_num):
        logger_client.info("__HANDLE_REQUEST__")

        with threading.Lock():
            with open(self._urls_file, "r") as fd:
                lines = islice(
                    fd,
                    th_num * self._num_threads,
                    (th_num + 1) * self._num_threads
                )
                for url in lines:
                    logger_client.info(f"__send: Thread({threading.current_thread().name}): {url}")

                    self.server.send(bytes(url, "utf-8"))



    def connect(self):
        # while True:
            
        logger_client.info("__PUSH_GET_ANS__")

        for th in self.threads:
            print(f"start {th}")
            th.start()

        for th in self.threads:
            print(f"join {th}")
            th.join()

        while True:
            ans = self.server.recv(1024).decode("utf-8")
            print(ans, end="\n\n")
            


if __name__ == "__main__":
    # console input
    parser = console_client_input()
    client_input = parser.parse_args(sys.argv[1:])

    create_urls("urls_global.txt")

    # Client
    # clnt = Client("urls_test.txt", client_input.m)
    clnt = Client(client_input.f, client_input.m)
    answer = clnt.connect()
