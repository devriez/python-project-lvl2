from gendiff.scripts.generate_diff import generate_diff

PATH_TO_FLAT1_JSON = 'gendiff/tests/fixtures/file1_flat.json'
PATH_TO_FLAT2_JSON = 'gendiff/tests/fixtures/file2_flat.json'
PATH_TO_FLAT1_YML = 'gendiff/tests/fixtures/file1_flat.yml'
PATH_TO_FLAT2_YML = 'gendiff/tests/fixtures/file2_flat.yml'
PATH_TO_NESTED1_JSON = 'gendiff/tests/fixtures/file1_nested.json'
PATH_TO_NESTED2_JSON = 'gendiff/tests/fixtures/file2_nested.json'
PATH_TO_NESTED1_YML = 'gendiff/tests/fixtures/file1_nested.yml'
PATH_TO_NESTED2_YML = 'gendiff/tests/fixtures/file2_nested.yml'

PATH_TO_STRING_RESULT_FLAT = 'gendiff/tests/fixtures/result_printdiff_flat.txt'
PATH_TO_STRING_RESULT_NESTED = 'gendiff/tests/fixtures/result_printdiff_nested.txt'

def test_generate_diff():
    f = open(PATH_TO_STRING_RESULT_FLAT)
    result_correct_flat = f.read()

    result_json_flat = generate_diff(PATH_TO_FLAT1_JSON, PATH_TO_FLAT2_JSON)
    assert result_json_flat == result_correct_flat

    result_yml_flat = generate_diff(PATH_TO_FLAT1_YML, PATH_TO_FLAT2_YML)
    assert result_yml_flat == result_correct_flat

    f = open(PATH_TO_STRING_RESULT_NESTED)
    result_correct_nested = f.read()

    result_json_nested = generate_diff(PATH_TO_NESTED1_JSON, PATH_TO_NESTED2_JSON)
    assert result_json_nested == result_correct_nested

    result_yml_nested = generate_diff(PATH_TO_NESTED1_YML, PATH_TO_NESTED2_YML)
    assert result_yml_nested == result_correct_nested
