import sys
import argparse
from urllib import request
from faker import Faker
import threading
import queue
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from bs4.element import Comment
import nltk


URLS_TXT = "urls.txt"
NUM_URLS = 100

def parse_client_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default=0)
    parser.add_argument("-f", default=URLS_TXT)
 
    return parser



# client
# class Client:
#     def __init__(self, urls_file, num_threads) -> None:
#         self._urls_file = urls_file
#         self._num_threads = num_threads

#         threads = [
#             threading.Thread(
#                 target=handle_request,
#                 args=(urls_file,),
#                 name="counter_example"
#             )
#             for _ in range(num_threads)
#         ]

#         self._sem = threading.Semaphore(10)

#     @staticmethod
#     def handle_request(self):
#         pass


if __name__ == "__main__":

    # parser = parse_client_input()
    # namespace = parser.parse_args(sys.argv[1:])

    # print (f"m={namespace.m}, f={namespace.f}")

    # with open(URLS_TXT, "w") as fd:
    #     URL = "https://infoselection.ru/infokatalog/internet-i-programmy/internet-osnovnoe/item/250-50-samykh-populyarnykh-internet-resursov-v-ssha"

    #     page = requests.get(URL)
    #     soup = BeautifulSoup(page.text, "lxml")

    #     table = soup.find("table", class_="tbscrol gentbl1 zebra4").find_all("a")
    #     # print(type(table))
    #     for i in range(NUM_URLS):
    #         url = table[i].get("href")
    #         fd.write(f"{url}\n")
            # print(table[i].get("href"))

#     from urllib.request import urlopen
# from bs4 import BeautifulSoup

    # url = "https://amazon.co.jp/"
    # html = urlopen(url).read()
    # soup = BeautifulSoup(html, features="html.parser")

    # # kill all script and style elements
    # for script in soup(["script", "style"]):
    #     script.extract()    # rip it out

    # # get text
    # text = soup.get_text()

    # # break into lines and remove leading and trailing space on each
    # lines = (line.strip() for line in text.splitlines())
    # # break multi-headlines into a line each
    # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # # drop blank lines
    # text = '\n'.join(chunk for chunk in chunks if chunk)
    # print(text)

    
    url = "https://uol.com.br/"    
    html = urlopen(url).read()    
    soup = BeautifulSoup(html, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())

    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk).split()
    print(len(text))




    # page = urlopen(URL)
    # parsed_html = BeautifulSoup(page, features="lxml")
    # print(parsed_html.body.find('div', attrs={'class' : 'container'}))#.text)


    # response = urlopen(URL) #requests.get(URL)
    # soup = BeautifulSoup(response, 'lxml')

    # # print(soup.body.find_all(text=True))

    # # allNews = soup.stripped_strings
    # print(len([text for text in soup.stripped_strings]))
    # # quotes = soup.find_all('span', class_='text')
