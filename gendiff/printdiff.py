

def print_diff(diff, indent=0):
    result = ['{']
    sorted_keys = sorted(diff.keys())

    for key in sorted_keys:
        if diff[key]['status1'] == 'added':
            result.append(f"{' ' * indent}  + {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'deleted':
            result.append(f"{' ' * indent}  - {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'unchanged':
            result.append(f"{' ' * indent}    {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'replaced':
            result.append(f"{' ' * indent}  - {key}: {diff[key]['body1']}")
            result.append(f"{' ' * indent}  + {key}: {diff[key]['body2']}")
        if diff[key]['status1'] == 'changed':
            indent += 2
            diff_nested = diff[key]['body1']
            result.append(f"{' ' * indent}    {key}: {print_diff(diff_nested, indent)}")

    result.append('}')
    return '\n'.join(result)
