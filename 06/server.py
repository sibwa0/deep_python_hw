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

    parser = parse_server_input()
    namespace = parser.parse_args(sys.argv[1:])

    print (f"w={namespace.k}, k={namespace.w}")
