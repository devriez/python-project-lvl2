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

def test_make_diff():
    result_flat_json = make_diff(PATH_TO_FLAT1_JSON, PATH_TO_FLAT2_JSON)
    assert result_flat_json == read_file(PATH_TO_RESULT_FLAT)

    #result_nested_json = make_diff(PATH_TO_NESTED1_JSON, PATH_TO_NESTED2_JSON)
    #assert result_nested_json == read_file(PATH_TO_RESULT_NESTED)

    result_flat_yml = make_diff(PATH_TO_FLAT1_YML, PATH_TO_FLAT2_YML)
    assert result_flat_yml == read_file(PATH_TO_RESULT_FLAT)

    #result_nested_yml = make_diff(PATH_TO_NESTED1_YML, PATH_TO_NESTED2_YML)
    #assert result_fnested_yml == read_file(PATH_TO_RESULT_NESTED)
