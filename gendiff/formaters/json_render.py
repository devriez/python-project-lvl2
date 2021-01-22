def _make_value(diff):
    '''
    Makу representation for key values,
     that are not dictionaries, formated as json

    Parameters:
        diff: key value (not a dictionary)

    Return:
        key value formated as json

    '''
    if type(diff) == str:
        return f'"{diff}"'
    if diff is None:
        return 'null'

    if type(diff) == bool:
        string = str(diff)
        return string.lower()

    return diff


def _make_string_from_template(diff, key):
    '''
    Choose representation for diff depending on key status:
    'added', 'deleted', 'unchanged', 'changed', replaced
    in json format.

    Parameters:
        diff: dictionary with diff result rows
        key: key of next diff iteration

    Return:
        string representation of diff in json
    '''
    key_value = diff[key]
    status = key_value['status1']
    template = {
        'added': (
            f'"{key}": {{"status1": "added", '
            f'"body1": {json_render(key_value.get("body1"), "no_sort")}}}'
            ),
        'deleted': (
            f'"{key}": {{"status1": "deleted", '
            f'"body1": {json_render(key_value.get("body1"), "no_sort")}}}'
            ),
        'unchanged': (
            f'"{key}": {{"status1": "unchanged", '
            f'"body1": {json_render(key_value.get("body1"), "no_sort")}}}'
            ),
        'replaced': (
            f'"{key}": {{"status1": "replaced", '
            f'"body1": {json_render(key_value.get("body1"), "no_sort")}, '
            f'"body2": {json_render(key_value.get("body2"), "no_sort")}}}'
            ),
        'changed': (
            f'"{key}": {{"status1": "changed", '
            f'"body1": {json_render(key_value.get("body1"),"sort")}}}'
            )
    }
    return template[status]


def json_render(diff, sort_flag='sort'):
    '''
    Format diff resuls as a json.
    Parameters:
        diff: Dictionary with the diff result rows.
        sort_flag: string indicate do we nee to sort keys or not.
            not sorted when key value was unchanged. doesn't have diff
    Returns:
        String of diff rows, formatted as a json.
    '''

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
