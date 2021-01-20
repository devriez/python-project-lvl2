from gendiff.formaters.json_render import json_render
from gendiff.readfile import read_file

PATH_TO_DIFF = 'tests/fixtures/result_makediff_nested.json'
PATH_TO_RESULT = 'tests/fixtures/result_json.txt'

def test_json():

    f = open(PATH_TO_RESULT)
    result_correct = f.read()
    diff = read_file(PATH_TO_DIFF)
    result = json_render(diff)
    assert result == result_correct
