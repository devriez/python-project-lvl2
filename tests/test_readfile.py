from gendiff.readfile import read_file

PATH_TO_FILE_1 = 'tests/fixtures/file_before.json'
FILE1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

def test_read_file():
    assert read_file(PATH_TO_FILE_1) == FILE1
