#! /usr/bin/env python3

import argparse
from gendiff.readfile import read_file
from gendiff.makediff import make_diff
from gendiff.selectformater import select_formater


def generate_diff(path1, path2, formater_name='stylish'):
    file1 = read_file(path1)
    file2 = read_file(path2)
    diff = make_diff(file1, file2)
    formater = select_formater(formater_name)
    return formater(diff)


def main():

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
