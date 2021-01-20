from gendiff.scripts.generate_diff import generate_diff

PATH_TO_JSON_BEFORE = 'tests/fixtures/file_before.json'
PATH_TO_JSON_AFTER = 'tests/fixtures/file_after.json'
PATH_TO_YML_BEFORE = 'tests/fixtures/file_before.yml'
PATH_TO_YML_AFTER = 'tests/fixtures/file_after.yml'
PATH_TO_RESULT_STYLISH = 'tests/fixtures/result_stylish.txt'
PATH_TO_RESULT_PLAIN = 'tests/fixtures/result_plain.txt'
PATH_TO_RESULT_JSON = 'tests/fixtures/result_json.txt'


def test_generate_diff():

    f = open(PATH_TO_RESULT_STYLISH)
    result_correct_stylish = f.read()
    result_stylish = generate_diff(
       PATH_TO_JSON_BEFORE, PATH_TO_JSON_AFTER, 'stylish')
    assert result_stylish == result_correct_stylish
    result_stylish = generate_diff(PATH_TO_YML_BEFORE, PATH_TO_YML_AFTER, 'stylish')
    assert result_stylish == result_correct_stylish

    f = open(PATH_TO_RESULT_PLAIN)
    result_correct_plain = f.read()
    result_plain = generate_diff(
       PATH_TO_JSON_BEFORE, PATH_TO_JSON_AFTER, 'plain')
    assert result_plain == result_correct_plain
    result_plain = generate_diff(PATH_TO_YML_BEFORE, PATH_TO_YML_AFTER, 'plain')
    assert result_plain == result_correct_plain

    f = open(PATH_TO_RESULT_JSON)
    result_correct_json = f.read()
    result_json = generate_diff(
       PATH_TO_JSON_BEFORE, PATH_TO_JSON_AFTER, 'json')
    assert result_json == result_correct_json
    result_json = generate_diff(PATH_TO_YML_BEFORE, PATH_TO_YML_AFTER, 'json')
    assert result_json == result_correct_json
