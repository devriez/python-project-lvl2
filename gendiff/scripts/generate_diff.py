#! /usr/bin/env python3

import argparse
from gendiff.readfile import read_json_file


def generate_diff(path1, path2):
    file1 = read_json_file(path1)
    file2 = read_json_file(path2)
    result = ['{']
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    all_keys_sorted = sorted(set(keys1 + keys2))
    for key in all_keys_sorted:
        if key in file1 and key in file2:
            if file1[key] != file2[key]:
                result.append(f'  - {key}: {file1[key]}')
                result.append(f'  + {key}: {file2[key]}')
            else:
                result.append(f'    {key}: {file1[key]}')
        elif key in file1 and key not in file2:
            result.append(f'  - {key}: {file1[key]}')
        else:
            result.append(f'  + {key}: {file2[key]}')

    result.append('}')
    return '\n'.join(result)


def main():

    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', action="store")
    parser.add_argument('second_file', action="store")
    parser.add_argument('-f', '--format', dest="format",
                        action="store", help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
