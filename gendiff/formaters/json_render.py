import json


def json_render(diff):
    result = diff.copy()
    return  json.dumps(diff)
