from gendiff.readfile import read_file

PATH_TO_FILE_1 = 'tests/fixtures/file_before.json'
FILE1 = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {
            "key": "value",
            "doge": {
                "wow": ""
            }
      }
    },
    "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
            "key": "value"
        }
    },
    "group2": {
        "abc": 12345,
        "deep": {
            "id": 45
        }
    }
  }


def test_read_file():
    assert read_file(PATH_TO_FILE_1) == FILE1
