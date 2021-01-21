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


def _make_string_from_template(diff, key):

    status = diff[key]['status1']
    template: {
        'added': (
            f'"{key}": {{"status1": "added", '
            f'"body1": {json_render(diff[key]["body1"], "no_sort")}}}'
            ),
        'deleted': (
            f'"{key}": {{"status1": "deleted", '
            f'"body1": {json_render(diff[key]["body1"], "no_sort")}}}'
            ),
        'unchanged': (
            f'"{key}": {{"status1": "unchanged", '
            f'"body1": {json_render(diff[key]["body1"], "no_sort")}}}'
            ),
        'replaced': (
            f'"{key}": {{"status1": "replaced", '
            f'"body1": {json_render(diff[key]["body1"], "no_sort")}, '
            f'"body2": {json_render(diff[key]["body2"], "no_sort")}}}'
            ),
        'changed': (
            f'"{key}": {{"status1": "changed", '
            f'"body1": {json_render(diff[key]["body1"],"sort")}}}'
            )
    }
    return template[status]


def json_render(diff, sort_flag='sort'):

    if type(diff) != dict:
        return _make_value(diff)

    result = ['{']

    if sort_flag == 'sort':
        keys = sorted(diff.keys())
    else:
        keys = diff.keys()

    counter = 0

    for key in keys:
        counter += 1
        string = _make_string_from_template(diff, key)
        if counter < len(keys):
            string += ', '
        result.append(string)

    result.append('}')
    return ''.join(result)
