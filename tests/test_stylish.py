from gendiff.formaters.stylish_render import stylish_render
from gendiff.readfile import read_file

PATH_TO_DIFF = 'tests/fixtures/result_makediff_nested.json'
PATH_TO_RESULT = 'tests/fixtures/result_printdiff_nested.txt'


def test_stylish():

    f = open(PATH_TO_RESULT)
    correct_result = f.read()
    diff = read_file(PATH_TO_DIFF)
    result = stylish_render(diff)
    assert result == correct_result
