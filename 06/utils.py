import argparse
import logging
import requests
from bs4 import BeautifulSoup

IP = "127.0.0.1"
PORT = 6663
URLS_TXT = "urls.txt"
NUM_URLS = 100
TOP100_URL = "https://infoselection.ru/infokatalog/internet-i-programmy/internet-osnovnoe/item/250-50-samykh-populyarnykh-internet-resursov-v-ssha"

# logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file, mode="w")        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# console input
# client
def console_client_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default=0, type=int)
    parser.add_argument("-f", default=URLS_TXT)
 
    return parser

# server
def console_server_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', default=0, type=int)
    parser.add_argument('-k', default=0, type=int)
 
    return parser


# create 100-urls file 
def create_urls(urls_file):
    with open(urls_file, "w") as fd:
        page = requests.get(TOP100_URL)
        soup = BeautifulSoup(page.text, "lxml")

        table = soup.find("table", class_="tbscrol gentbl1 zebra4").find_all("a")

        for i in range(NUM_URLS):
            url = table[i].get("href")
            fd.write(f"{url}\n")
