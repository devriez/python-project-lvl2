def make_diff(file1, file2=None):

    if type(file1) != dict:
        return file1

    if file2 is None:
        file2 = file1

    keys1 = list(file1.keys())
    keys2 = list(file2.keys())

    all_keys = keys1 if (file1 == file2) else set(keys1 + keys2)

    result = {}

    for key in all_keys:
        if key in file1 and key not in file2:
            result[key] = {
                'status1': 'deleted',
                'body1': make_diff(file1[key])
                }
        elif key in file2 and key not in file1:
            result[key] = {
                'status1': 'added',
                'body1': make_diff(file2[key])
                }
        else:
            if file1[key] == file2[key]:
                result[key] = {
                    'status1': 'unchanged',
                    'body1': make_diff(file1[key])
                    }
            elif (type(file1[key]) != dict) or (type(file2[key]) != dict):
                result[key] = {
                    'status1': 'replaced',
                    'body1': make_diff(file1[key]),
                    'body2': make_diff(file2[key])
                    }
            else:
                result[key] = {
                    'status1': 'changed',
                    'body1': make_diff(file1[key], file2[key])
                    }

    return result
