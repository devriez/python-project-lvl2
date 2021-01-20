from gendiff.formaters.stylish import stylish
from gendiff.readfile import read_file

PATH_TO_JSON_FLAT = 'tests/fixtures/result_makediff_flat.json'
PATH_TO_STRING_FLAT = 'tests/fixtures/result_printdiff_flat.txt'
PATH_TO_JSON_NESTED = 'tests/fixtures/result_makediff_nested.json'
PATH_TO_STRING_NESTED = 'tests/fixtures/result_printdiff_nested.txt'


def test_stylish():
    f = open(PATH_TO_STRING_FLAT)
    correct_result_flat = f.read()
    result_json_flat = read_file(PATH_TO_JSON_FLAT)
    result_flat = stylish(result_json_flat)
    assert result_flat == correct_result_flat

    f = open(PATH_TO_STRING_NESTED)
    correct_result_nested = f.read()
    result_json_nested = read_file(PATH_TO_JSON_NESTED)
    result_nested = stylish(result_json_nested)
    assert result_nested == correct_result_nested
