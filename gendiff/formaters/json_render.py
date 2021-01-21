import json


def _make_value(diff):
    if type(diff) == str:
        return f'"{diff}"'
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
        counter = 0

        for key in keys:
            counter += 1
            if diff[key]['status1'] == 'added':
                string =f'"{key}": {{"status1": "added", "body1": {inner(diff[key]["body1"], layer)}}}'
            if diff[key]['status1'] == 'deleted':
                string =f'"{key}": {{"status1": "deleted", "body1": {inner(diff[key]["body1"], layer)}}}'
            if diff[key]['status1'] == 'unchanged':
                string =f'"{key}": {{"status1": "unchanged", "body1": {inner(diff[key]["body1"], layer)}}}'
            if diff[key]['status1'] == 'replaced':
                string =f'"{key}": {{"status1": "replaced", "body1": {inner(diff[key]["body1"], layer)}, "body2": {inner(diff[key]["body2"], layer)}}}'
            if diff[key]['status1'] == 'changed':
                string =f'"{key}": {{"status1": "changed", "body1": {inner(diff[key]["body1"], layer, "sort")}}}'
            if counter < len(keys):
                string += ', '
            result.append(string)

        result.append('}')
        return ''.join(result)

    return inner(diff)
