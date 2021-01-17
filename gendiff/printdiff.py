def print_diff(diff, indent=0, sort_flag='no_need_to_sort'):

    if type(diff) != dict:
        return diff

    step = ' ' * indent
    next_indent = indent + 4
    result = ['{']
    keys = diff.keys()
    if indent == 0 or sort_flag == 'sort':
        keys = sorted(keys)

    for key in keys:
        if diff[key]['status1'] == 'added':
            result.append(f"{step}  + {key}: {print_diff(diff[key]['body1'], next_indent)}")
        if diff[key]['status1'] == 'deleted':
            result.append(f"{step}  - {key}: {print_diff(diff[key]['body1'], next_indent)}")
        if diff[key]['status1'] == 'unchanged':
            result.append(f"{step}    {key}: {print_diff(diff[key]['body1'], next_indent)}")
        if diff[key]['status1'] == 'replaced':
            result.append(f"{step}  - {key}: {print_diff(diff[key]['body1'], next_indent)}")
            result.append(f"{step}  + {key}: {print_diff(diff[key]['body2'], next_indent)}")
        if diff[key]['status1'] == 'changed':
            next_indent = indent + 4
            diff_nested = diff[key]['body1']
            result.append(f"{step}    {key}: {print_diff(diff_nested, next_indent, 'sort')}")

    result.append(f'{step}}}')
    return '\n'.join(result)
