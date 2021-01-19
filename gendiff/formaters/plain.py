def _make_value(value):
    if type(value) == dict or type(value) == list:
        return '[complex value]'
    if type(value) == bool:
        return str(value).lower()
    if value is None:
        return 'null' 
    return value

def _make_string_from_template(path, diff, key):
    template = {
        'added': (
            f"Property '{path}' was added with value: "
            f"{_make_value(diff[key]['body1'])}"
            ),
        'deleted': f"Property '{path}' was removed",
        'removed': (
            f"Property '{path}' was updated. "
            f"From '{_make_value(diff[key]['body1'])}' "
            f"to '{_make_value(diff[key]['body2'])}'"
            )
    }
    status = diff[key]['status1']
    return template[status]

def _make_string(diff, path):
    keys = sorted(diff.keys())

    for key in keys:
        path = path + '.' + key
        if diff[key]['status1'] == 'added':
            return _make_string_from_template(path, diff, key)
        if diff[key]['status1'] == 'deleted':
            return _make_string_from_template(path, diff, key)
        if diff[key]['status1'] == 'removed':
            return _make_string_from_template(path, diff, key)
        if diff[key]['status1'] == 'changed':
            return _make_string(diff[key]['body1'], path) 

            
def plain(diff):
    result=[]
    keys = sorted(diff.keys())

    for key in keys:
        string = _make_string(diff[key]['body1'], key)
        result.append(string)

    return '/n'.join(result)    
