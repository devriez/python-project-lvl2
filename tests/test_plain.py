from gendiff.formaters.plain_render import plain_render
from gendiff.readfile import read_file

PATH_TO_DIFF = 'tests/fixtures/result_makediff.json'
PATH_TO_RESULT = 'tests/fixtures/result_plain.txt'


def test_plain():

    f = open(PATH_TO_RESULT)
    correct_result = f.read()
    diff = read_file(PATH_TO_DIFF)
    result = plain_render(diff)
    assert result == correct_result
