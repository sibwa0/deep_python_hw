from urllib.request import urlopen
import argparse
import sys


def parse_server_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', default=0)
    parser.add_argument('-k', default=0)
 
    return parser


# server 
class Server:
    def __init__(self, workers):
        self._workers = workers



if __name__ == "__main__":
    glued_urls = "http//123\n"

    glued_urls = glued_urls.replace("\n", "")
    http_start = glued_urls.find("http")
    http_end = glued_urls[1:].find("http")

    while http_start != -1:
        if http_end == -1:
            url = glued_urls[:]
            print(f"{url =}")
            break
        url = glued_urls[:http_end + 1]
        print(f"{url =}")
        http_start = http_end + 1
        glued_urls = glued_urls[http_start:]
        http_end = glued_urls[1:].find("http")

        

    print(glued_urls)
    print(glued_urls[http_start:http_end])
    print()
    print(f"{http_start =}")
    print(f"{http_end =}")
    
