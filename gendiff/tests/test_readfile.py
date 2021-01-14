from gendiff.readfile import read_file


def test_read_file():
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

    assert read_file('gendiff/tests/fixtures/file1.json') == file1
    assert read_file('gendiff/tests/fixtures/file2.json') == file2
