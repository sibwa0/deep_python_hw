import socket
import argparse
import sys
from faker import Faker
import threading
import requests
from bs4 import BeautifulSoup
import logging


# constants
logging.basicConfig(level=logging.INFO, filename="client_info.log", filemode="w")
IP = "127.0.0.1"
PORT = 1111
URLS_TXT = "urls.txt"
NUM_URLS = 100
URL = "https://infoselection.ru/infokatalog/internet-i-programmy/internet-osnovnoe/item/250-50-samykh-populyarnykh-internet-resursov-v-ssha"


# console input 
def console_client_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default=0, type=int)
    parser.add_argument("-f", default=URLS_TXT)
 
    return parser


# create 100-urls file 
def create_urls(urls_file):
    with open(urls_file, "w") as fd:
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "lxml")

        table = soup.find("table", class_="tbscrol gentbl1 zebra4").find_all("a")

        for i in range(NUM_URLS):
            url = table[i].get("href")
            fd.write(f"{url}\n")


class Client:
    def __init__(self, urls_file, num_threads) -> None:
        logging.info("__INIT__")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((IP, PORT))

        # self._urls_file = urls_file
        # self._size_urls = size_urls
        self._num_threads = num_threads

        self.threads = [
            threading.Thread(
                target=self.handle_request,
                args=(urls_file,),
                name=f"{i} Thread"
            )
            for i in range(self._num_threads)
        ]
    

    def handle_request(self, urls_file):
        logging.info("__HANDLE_REQUEST__")
        with open(urls_file, "r") as fd:
            url = fd.readline()
            while url != "":
                self.server.send(bytes(url, "utf-8"))

                url = fd.readline()

    def push_and_get_ans(self):
        logging.info("__PUSH_GET_ANS__")
        for th in self.threads:
            print(f"start {th}")
            th.start()

        for th in self.threads:
            print(f"join {th}")
            th.join()

        return self.server.recv(1024).decode("utf-8")


if __name__ == "__main__":
    # console input
    parser = console_client_input()
    client_input = parser.parse_args(sys.argv[1:])
    # print (f"m={namespace.m}, f={namespace.f}")

    create_urls(client_input.f)

    clnt = Client(client_input.f, client_input.m)
    answer = clnt.push_and_get_ans()
    print(f"Recieve from Server: {answer}")



    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server.connect((IP, PORT))

    # string = input("Enter string: ")
    # server.send(bytes(string, "utf-8"))
    # buffer = server.recv(1024).decode("utf-8")
    
    # print(f"Recieve from Server: {buffer}")
