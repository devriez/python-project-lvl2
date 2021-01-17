from gendiff.makediff import make_diff
from gendiff.readfile import read_file

PATH_TO_FLAT1_JSON = 'gendiff/tests/fixtures/file1_flat.json'
PATH_TO_FLAT2_JSON = 'gendiff/tests/fixtures/file2_flat.json'
PATH_TO_FLAT1_YML = 'gendiff/tests/fixtures/file1_flat.yml'
PATH_TO_FLAT2_YML = 'gendiff/tests/fixtures/file2_flat.yml'
PATH_TO_RESULT_FLAT = 'gendiff/tests/fixtures/result_makediff_flat.json'
PATH_TO_NESTED1_JSON = 'gendiff/tests/fixtures/file1_nested.json'
PATH_TO_NESTED2_JSON = 'gendiff/tests/fixtures/file2_nested.json'
PATH_TO_NESTED1_YML = 'gendiff/tests/fixtures/file1_nested.yml'
PATH_TO_NESTED2_YML = 'gendiff/tests/fixtures/file2_nested.yml'
PATH_TO_RESULT_NESTED = 'gendiff/tests/fixtures/result_makediff_nested.json'
PATH_TO_NESTED1_JSON_SHORT = 'gendiff/tests/fixtures/file1_nested_short.json'
PATH_TO_NESTED2_JSON_SHORT = 'gendiff/tests/fixtures/file2_nested_short.json'
PATH_TO_RESULT_NESTED_SHORT = 'gendiff/tests/fixtures/result_makediff_nested_short.json'

def test_make_diff():
    flat1_json = read_file(PATH_TO_FLAT1_JSON)
    flat2_json = read_file(PATH_TO_FLAT2_JSON)
    result_flat_json = make_diff(flat1_json, flat2_json)
    assert result_flat_json == read_file(PATH_TO_RESULT_FLAT)

#need to fix data in short fixtures
#    nested1_json_short = read_file(PATH_TO_NESTED1_JSON_SHORT)
#    nested2_json_short = read_file(PATH_TO_NESTED2_JSON_SHORT)
#    result_nested_json_short = make_diff(nested1_json_short, nested2_json_short)
#    correct_result_nested_short = read_file(PATH_TO_RESULT_NESTED_SHORT)
#    assert result_nested_json_short == correct_result_nested_short

    nested1_json = read_file(PATH_TO_NESTED1_JSON)
    nested2_json = read_file(PATH_TO_NESTED2_JSON)
    result_nested_json = make_diff(nested1_json, nested2_json)
    correct_result_nested = read_file(PATH_TO_RESULT_NESTED)
    assert result_nested_json == correct_result_nested

    flat1_yml = read_file(PATH_TO_FLAT1_YML)
    flat2_yml = read_file(PATH_TO_FLAT2_YML)
    result_flat_yml = make_diff(flat1_yml, flat2_yml)
    assert result_flat_yml == read_file(PATH_TO_RESULT_FLAT)

    nested1_yml = read_file(PATH_TO_NESTED1_YML)
    nested2_yml = read_file(PATH_TO_NESTED2_YML)
    result_nested_yml = make_diff(nested1_yml, nested2_yml)
    correct_result_nested = read_file(PATH_TO_RESULT_NESTED)
    assert result_nested_yml == correct_result_nested
