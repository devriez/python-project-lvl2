from gendiff.scripts.generate_diff import generate_diff

PATH_TO_JSON_BEFORE = 'tests/fixtures/file_before.json'
PATH_TO_JSON_AFTER = 'tests/fixtures/file_after.json'
PATH_TO_YML_BEFORE = 'tests/fixtures/file_before.yml'
PATH_TO_YML_AFTER = 'tests/fixtures/file_after.yml'
PATH_TO_RESULT = 'tests/fixtures/result_printdiff.txt'


def test_generate_diff():

    f = open(PATH_TO_RESULT)
    result_correct = f.read()

    result = generate_diff(
       PATH_TO_JSON_BEFORE, PATH_TO_JSON_AFTER)
    assert result == result_correct

    result = generate_diff(PATH_TO_YML_BEFORE, PATH_TO_YML_AFTER)
    assert result == result_correct
