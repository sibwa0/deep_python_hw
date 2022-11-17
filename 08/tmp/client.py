import socket
import sys
import threading
from itertools import islice

from utils import IP, PORT, console_client_input, setup_logger

# constants
logger_client = setup_logger('first_logger', 'client_logfile.log')


class Client:
    def __init__(self, urls_file, num_threads) -> None:
        logger_client.info("__INIT__")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
            with open(self._urls_file, "r", encoding='utf-8') as file_d:
                lines = islice(
                    file_d,
                    th_num * self._num_threads,
                    (th_num + 1) * self._num_threads
                )
                for url in lines:
                    logger_client.info(
                        "__send: %s: %s",
                        threading.current_thread().name,
                        url
                    )

                    self.server.send(bytes(url, "utf-8"))

    def connect(self):

        logger_client.info("__Connect__")
        self.server.connect(("localhost", PORT))

        for thread in self.threads:
            logger_client.info("__start %s", thread)
            thread.start()

        for _ in range(100):
            ans = self.server.recv(1024).decode("utf-8")
            print(ans, end="\n\n")

        self.server.close()


if __name__ == "__main__":
    # console input
    parser = console_client_input()
    client_input = parser.parse_args(sys.argv[1:])

    # create_urls("urls_global.txt")

    clnt = Client(client_input.f, client_input.m)
    clnt.connect()
