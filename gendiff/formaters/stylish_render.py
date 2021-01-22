def _make_value(diff):
    '''
     Makу representation for key values,
     that are not dictionary

    Parameters:
        diff: difference that are not dictionary

    Return:
        string format for 'None" and boolean
        string as string, and numbers

    '''
    if diff is None:
        return 'null'

    if type(diff) == bool:
        string = str(diff)
        return string.lower()

    return diff


def stylish_render(diff):
    '''
    Format diff resuls in stylish format.
    Parameters:
        diff: Dictionaru with the diff result rows.
    Returns:
        String of diff rows, structured by indents.
    '''

    def inner(diff, indent=0, sort_flag='no_need_to_sort'):

        if type(diff) != dict:
            return _make_value(diff)

        step = ' ' * indent
        result = ['{']

        if indent == 0 or sort_flag == 'sort':
            keys = sorted(diff.keys())
        else:
            keys = diff.keys()

        indent = indent + 4

        for key in keys:
            if diff[key]['status1'] == 'added':
                string = (
                    f"{step}  + {key}: "
                    f"{inner(diff[key]['body1'], indent)}"
                    )
            if diff[key]['status1'] == 'deleted':
                string = (
                    f"{step}  - {key}: "
                    f"{inner(diff[key]['body1'], indent)}"
                    )
            if diff[key]['status1'] == 'unchanged':
                string = (
                    f"{step}    {key}: "
                    f"{inner(diff[key]['body1'], indent)}"
                    )
            if diff[key]['status1'] == 'replaced':
                string = (
                    f"{step}  - {key}: {inner(diff[key]['body1'], indent)}"
                    '\n'
                    f"{step}  + {key}: {inner(diff[key]['body2'], indent)}"
                    )
            if diff[key]['status1'] == 'changed':
                diff_inner = diff[key]['body1']
                string = (
                    f"{step}    {key}: "
                    f"{inner(diff_inner, indent, 'sort')}"
                    )
            result.append(string)

        result.append(f'{step}}}')
        return '\n'.join(result)

    return inner(diff)
