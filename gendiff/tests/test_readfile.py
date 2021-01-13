from gendiff.readfile import read_json_file


def test_read_json_file():
    file1 = {
      "host": "hexlet.io",
      "timeout": 50,
      "proxy": "123.234.53.22",
      "follow": False
    }
    file2 = {
      "timeout": 20,
      "verbose": True,
      "host": "hexlet.io"
    }

    assert read_json_file('gendiff/tests/fixtures/file1.json') == file1
    assert read_json_file('gendiff/tests/fixtures/file2.json') == file2
