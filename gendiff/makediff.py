def make_diff(dict1, dict2=None):
    """
    Generate a diff for a given dictionaries.
    Parameters:
        dict1: The first dictionary to compare.
        dict2: The second dictionary to compare.
    Returns:
        Diff of the given dictionaries.
    """
    if type(dict1) != dict:
        return dict1

    if dict2 is None:
        dict2 = dict1

    keys = _collect_keys(dict1, dict2)

    result = {}

    for key in keys:
        if key in dict1 and key not in dict2:
            result[key] = {
                'status1': 'deleted',
                'body1': make_diff(dict1[key])
            }
        elif key in dict2 and key not in dict1:
            result[key] = {
                'status1': 'added',
                'body1': make_diff(dict2[key])
            }
        else:
            if dict1[key] == dict2[key]:
                result[key] = {
                    'status1': 'unchanged',
                    'body1': make_diff(dict1[key])
                }
            elif (type(dict1[key]) != dict) or (type(dict2[key]) != dict):
                result[key] = {
                    'status1': 'replaced',
                    'body1': make_diff(dict1[key]),
                    'body2': make_diff(dict2[key])
                }
            else:
                result[key] = {
                    'status1': 'changed',
                    'body1': make_diff(dict1[key], dict2[key])
                }

    return result


def _collect_keys(dict1, dict2):

    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())

    return keys1 if (dict1 == dict2) else set(keys1 + keys2)
