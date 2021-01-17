from gendiff.printdiff import print_diff
from gendiff.readfile import read_file

PATH_TO_JSON_RESULT_FLAT = 'gendiff/tests/fixtures/result_makediff_flat.json'
PATH_TO_STRING_RESULT_FLAT = 'gendiff/tests/fixtures/result_printdiff_flat.txt'
PATH_TO_JSON_RESULT_NESTED = 'gendiff/tests/fixtures/result_makediff_nested.json'
PATH_TO_STRING_RESULT_NESTED = 'gendiff/tests/fixtures/result_printdiff_nested.txt'
PATH_TO_JSON_RESULT_NESTED_SHORT = 'gendiff/tests/fixtures/result_makediff_nested_short.json'
PATH_TO_STRING_RESULT_NESTED_SHORT = 'gendiff/tests/fixtures/result_printdiff_nested_short.txt'


def test_print_diff():
    f = open(PATH_TO_STRING_RESULT_FLAT)
    correct_result_flat = f.read()
    result_json_flat = read_file(PATH_TO_JSON_RESULT_FLAT)
    result_flat = print_diff(result_json_flat)
    print('result', result_flat)
    print('correct_result', correct_result_flat)
    assert result_flat == correct_result_flat

    f = open(PATH_TO_STRING_RESULT_NESTED_SHORT)
    correct_result_nested_short = f.read()
    result_json_nested_short = read_file(PATH_TO_JSON_RESULT_NESTED_SHORT)
    result_nested_short = print_diff(result_json_nested_short)
    print('result', result_nested_short)
    print('correct_result', correct_result_nested_short)
    assert result_nested_short == correct_result_nested_short

    f = open(PATH_TO_STRING_RESULT_NESTED)
    correct_result_nested = f.read()
    result_json_nested = read_file(PATH_TO_JSON_RESULT_NESTED)
    result_nested = print_diff(result_json_nested)
    print('result', result_nested)
    print('correct_result', correct_result_nested)
    assert result_nested == correct_result_nested
