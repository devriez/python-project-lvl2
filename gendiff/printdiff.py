def print_diff(diff, indent=0):
    print('diff', diff)
    if type(diff) != dict:
        return diff

    step = ' ' * indent
    next_indent = indent + 4
    result = ['{']
    sorted_keys = sorted(diff.keys())

    print('keys', list(diff.keys()))
    print('sorted_keys', sorted_keys)

    for key in sorted_keys:
        print('key', key)
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
            result.append(f"{step}    {key}: {print_diff(diff_nested, next_indent)}")

    result.append(f'{step}}}')
    return '\n'.join(result)
