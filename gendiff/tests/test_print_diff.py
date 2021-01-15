from gendiff.printdiff import print_diff
from gendiff.readfile import read_file

PATH_TO_JSON_RESULT_FLAT = 'gendiff/tests/fixtures/result_makediff_flat.json'
PATH_TO_STRING_RESULT_FLAT = 'gendiff/tests/fixtures/result_printdiff_flat.txt'
PATH_TO_JSON_RESULT_NESTED = 'gendiff/tests/fixtures/result_makediff_nested.json'
PATH_TO_STRING_RESULT_NESTED = 'gendiff/tests/fixtures/result_printdiff_nested.txt'


def test_print_diff():
    f = open(PATH_TO_STRING_RESULT_FLAT)
    correct_result_flat = f.read()
    result_flat = print_diff(PATH_TO_JSON_RESULT_FLAT)

    assert result_flat == correct_result_flat

    f = open(PATH_TO_STRING_RESULT_NESTED)
    correct_result_nested = f.read()
    result_nested = print_diff(PATH_TO_JSON_RESULT_NESTED)

    assert result_nested == correct_result_nested