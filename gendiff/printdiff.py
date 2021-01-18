def stylish(diff, indent=0, sort_flag='no_need_to_sort'):

    if diff is None:
        return 'null'

    if type(diff) == bool:
        string = str(diff)
        return string.lower()

    if type(diff) != dict:
        return diff

    step = ' ' * indent
    indent = indent + 4
    result = ['{']

    if indent == 0 or sort_flag == 'sort':
        keys = sorted(diff.keys())
    else:
        keys = diff.keys()

    for key in keys:
        if diff[key]['status1'] == 'added':
            string = f"{step}  + {key}: {stylish(diff[key]['body1'], indent)}"
        if diff[key]['status1'] == 'deleted':
            string = f"{step}  - {key}: {stylish(diff[key]['body1'], indent)}"
        if diff[key]['status1'] == 'unchanged':
            string = f"{step}    {key}: {stylish(diff[key]['body1'], indent)}"
        if diff[key]['status1'] == 'replaced':
            string = f"{step}  - {key}: {stylish(diff[key]['body1'], indent)}"
            string = f"{step}  + {key}: {stylish(diff[key]['body2'], indent)}"
        if diff[key]['status1'] == 'changed':
            diff_inner = diff[key]['body1']
            string = f"{step}    {key}: {stylish(diff_inner, indent, 'sort')}"
        result.append(string)

    result.append(f'{step}}}')
    return '\n'.join(result)
