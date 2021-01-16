#def make_string(diff, result, sign, key, body)
#    return result.append(f"  {sign} {key}: {diff[key]['body1']}")

def print_diff(diff):
    result = ['{']
    sorted_keys = sorted(diff.keys())

    for key in sorted_keys:
        if diff[key]['status1'] == 'add':
            #make_string(diff, result, "+", key, body)
            result.append(f"  + {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'deleted':
            result.append(f"  - {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'unchanged':
            result.append(f"    {key}: {diff[key]['body1']}")
        if diff[key]['status1'] == 'replaced':
            result.append(f"  - {key}: {diff[key]['body1']}")
            result.append(f"  + {key}: {diff[key]['body2']}")        
        if diff[key]['status1'] == 'changed':
            diff_nested = diff[key]['body1']
            result.append(f"    {key}: {print_diff(diff_nested)}")

    result.append('}')
    return '\n'.join(result)
