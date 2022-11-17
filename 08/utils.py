import argparse
import logging
from bs4 import BeautifulSoup


URLS_TXT = "urls_copy.txt"
NUM_URLS = 100


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
def console_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", default=0, type=int)
    parser.add_argument("-f", default=URLS_TXT)
 
    return parser