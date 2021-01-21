# def json_render(diff):

#     def inner(diff, sort_flag='sort'):

#         if type(diff) != dict:
#             return _make_value(diff)

#         result = ['{']

#         if sort_flag == 'sort':
#             keys = sorted(diff.keys())
#         else:
#             keys = diff.keys()

#         counter = 0

#         for key in keys:
#             counter += 1
#             if diff[key]['status1'] == 'added':
#                 string =f'"{key}": {{"status1": "added", "body1": {inner(diff[key]["body1"], "no_sort")}}}'
#             if diff[key]['status1'] == 'deleted':
#                 string =f'"{key}": {{"status1": "deleted", "body1": {inner(diff[key]["body1"], "no_sort")}}}'
#             if diff[key]['status1'] == 'unchanged':
#                 string =f'"{key}": {{"status1": "unchanged", "body1": {inner(diff[key]["body1"], "no_sort")}}}'
#             if diff[key]['status1'] == 'replaced':
#                 string =f'"{key}": {{"status1": "replaced", "body1": {inner(diff[key]["body1"], "no_sort")}, "body2": {inner(diff[key]["body2"], "no_sort")}}}'
#             if diff[key]['status1'] == 'changed':
#                 string =f'"{key}": {{"status1": "changed", "body1": {inner(diff[key]["body1"],"sort")}}}'
#             if counter < len(keys):
#                 string += ', '
#             result.append(string)

#         result.append('}')
#         return ''.join(result)

#     return inner(diff)