from gendiff.formaters.plain import plain
from gendiff.readfile import read_file

PATH_TO_JSON_NESTED = 'gendiff/tests/fixtures/result_makediff_nested.json'
PATH_TO_PLAIN = 'gendiff/tests/fixtures/result_plain.txt'


def test_plain():

    f = open(PATH_TO_PLAIN)
    correct_result_plain = f.read()
    result_json_nested = read_file(PATH_TO_JSON_NESTED)
    result_plain = plain(result_json_nested)
    assert result_plain == correct_result_plain