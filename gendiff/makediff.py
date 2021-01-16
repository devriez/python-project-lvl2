from gendiff.readfile import read_file


def make_diff(file1, file2):
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    result = {}
    all_keys = set(keys1 + keys2)

    for key in all_keys:
        if key in file1 and key not in file2:
            result[key] = {'status1': 'deleted', 'body1': file1[key]}
        elif key in file2 and key not in file1:
            result[key] = {'status1': 'added', 'body1': file2[key]}
        else:
            if file1[key] == file2[key]:
                result[key] = {'status1': 'unchanged', 'body1': file1[key]}
            elif (type(file1[key]) != dict) or (type(file2[key]) != dict):
                result[key] = {'status1': 'replaced', 'body1': file1[key], 'body2': file2[key]}
            else:
                result[key] = {'status1': 'changed', 'body1': make_diff(file1[key], file2[key])}

    return result

