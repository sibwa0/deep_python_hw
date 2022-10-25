import argparse


def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', default=0)
    parser.add_argument('-k', default=0)
 
    return parser
