

def print_diff(diff, indent=0):
    step = ' ' * indent
    result = ['{']
    sorted_keys = sorted(diff.keys())

    for key in sorted_keys:
        if diff[key]['status1'] == 'added':
            result.append(f"{step}  + {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'deleted':
            result.append(f"{step}  - {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'unchanged':
            result.append(f"{step}    {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'replaced':
            result.append(f"{step}  - {key}: {diff[key]['body1']}")
            result.append(f"{step}  + {key}: {diff[key]['body2']}")
        if diff[key]['status1'] == 'changed':
            next_indent = indent + 2
            diff_nested = diff[key]['body1']
            result.append(f"{step}    {key}: {print_diff(diff_nested, next_indent)}")

    result.append('}')
    return '\n'.join(result)
