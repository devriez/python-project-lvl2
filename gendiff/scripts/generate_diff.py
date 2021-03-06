#! /usr/bin/env python3

import argparse
from gendiff.gendiff import generate_diff


def main():
    """Launch a gendiff cli."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', action="store")
    parser.add_argument('second_file', action="store")
    parser.add_argument('-f', '--format', dest="format",
                        action="store", help='set format of output')
    args = parser.parse_args()
    if not args.format:
        args.format = 'stylish'
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
