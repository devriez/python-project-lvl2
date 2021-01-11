#! /usr/bin/env python3

import argparse


def main():

    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', action="store")
    parser.add_argument('second_file', action="store")
    parser.add_argument('-f', '--format', dest="format", action="store", help='set format of output')

    args = parser.parse_args()
   # print(args)

if __name__ == '__main__':
    main()
