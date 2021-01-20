from gendiff.formaters.json_render import json_render
from gendiff.readfile import read_file

PATH_TO_JSON = 'gendiff/tests/fixtures/result_makediff_nested.json'
PATH_TO_RESULT = 'gendiff/tests/fixtures/result_json.txt'

def test_json():

    f = open(PATH_TO_RESULT)
    result_correct = f.read()
    result_json = read_file(PATH_TO_JSON)
    result_json_to_string = json_render(result_json)
    assert result_json_to_string == result_correct
