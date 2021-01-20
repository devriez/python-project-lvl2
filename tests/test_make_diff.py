from gendiff.makediff import make_diff
from gendiff.readfile import read_file

PATH_TO_JSON_BEFORE = 'tests/fixtures/file1_nested.json'
PATH_TO_JSON_AFTER = 'tests/fixtures/file2_nested.json'
PATH_TO_YML_BEFORE = 'tests/fixtures/file1_nested.yml'
PATH_TO_YML_AFTER = 'tests/fixtures/file2_nested.yml'
PATH_TO_RESULT = 'tests/fixtures/result_makediff_nested.json'


def test_make_diff():

    correct_result = read_file(PATH_TO_RESULT)

    json_before = read_file(PATH_TO_JSON_BEFORE)
    json_after = read_file(PATH_TO_JSON_AFTER)
    result = make_diff(json_before, json_after)
    assert result == correct_result

    yml_before = read_file(PATH_TO_YML_BEFORE)
    yml_after = read_file(PATH_TO_YML_AFTER)
    result = make_diff(yml_before, yml_after)
    assert result == correct_result
