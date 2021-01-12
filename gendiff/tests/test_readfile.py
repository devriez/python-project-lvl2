from gendiff.tests import read_json_file


def test_read_json_file():
    file1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
    }
    file2 = {
    "timeout": 20,
    "verbose": true,
    "host": "hexlet.io"
    }

    asssert read_json_file('./fixtures/file1.json') == file1
    asssert read_json_file('./fixtures/file2.json') == file2
