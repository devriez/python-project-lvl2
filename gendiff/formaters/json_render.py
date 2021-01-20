import json


def json_to_string(diff):
    json_to_dict = json.loads(diff)
    dict_to_json_to_string = json.dumps(json_to_dict)
    return  dict_to_json_to_string   