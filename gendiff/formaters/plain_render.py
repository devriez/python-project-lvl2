def _make_value(value):
    if type(value) == dict or type(value) == list:
        return '[complex value]'
    if type(value) == bool:
        return str(value).lower()
    if value is None:
        return 'null'
    if type(value) == str:
        return f"'{value}'"
    return value


def _make_string_from_template(path, diff, key):
    template = {
        'added': (
            f"Property '{path}' was added with value: "
            f"{_make_value(diff[key]['body1'])}"
            ),
        'deleted': f"Property '{path}' was removed",
        'replaced': (
            f"Property '{path}' was updated. "
            f"From {_make_value(diff[key]['body1'])} "
            f"to {_make_value(diff[key].get('body2'))}"
            )
    }
    status = diff[key]['status1']

    return template[status]


def plain_render(diff, path=''):
    print('diff in plain_render', diff)
    keys = sorted(diff.keys())
    result = []

    for key in keys:
        path_to_value = path + key
        if diff[key]['status1'] == 'unchanged':
            continue
        elif diff[key]['status1'] == 'changed':
            string = plain_render(diff[key]['body1'], path_to_value + '.')
        else:
            string = _make_string_from_template(path_to_value, diff, key)
        result.append(string)

    return '\n'.join(result)
