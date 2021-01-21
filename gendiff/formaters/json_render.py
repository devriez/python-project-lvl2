import json


# def json_render(diff):
#     result = diff.copy()
#     return  json.dumps(diff)

def _make_value(diff):
    if diff is None:
        return 'null'

    if type(diff) == bool:
        string = str(diff)
        return string.lower()

    return diff


def json_render(diff):

    def inner(diff, layer=0, sort_flag='no_need_to_sort'):

        if type(diff) != dict:
            return _make_value(diff)

        result = ['{']

        if layer == 0 or sort_flag == 'sort':
            keys = sorted(diff.keys())
        else:
            keys = diff.keys()

        layer = layer + 1

        for key in keys:
            if diff[key]['status1'] == 'added':
                string = '"()": {"status1": "added", "body1": {()}}'.format(key, inner(diff[key]['body1'], layer))
            if diff[key]['status1'] == 'deleted':
                string = '"()": {"status1": "deleted", "body1": {()}}'.format(key, inner(diff[key]['body1'], layer))
            if diff[key]['status1'] == 'unchanged':
                string = '"()": {"status1": "added", "ubody1": {()}}'.format(key, inner(diff[key]['body1'], layer))
            if diff[key]['status1'] == 'replaced':
                string = '"()": {"status1": "replaced", "body1": {()}, "body2": {()}}'.format(key, inner(diff[key]['body1'], layer), inner(diff[key]['body2'], layer))
            if diff[key]['status1'] == 'changed':
                string = '"()": {"status1": "changed", "body1": {()}}'.format(key, inner(diff[key]['body1'], layer, 'sort'))
            result.append(string)

        result.append('}')
        return ''.join(result)

    return inner(diff)
