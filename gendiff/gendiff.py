from gendiff.makediff import make_diff
from gendiff.readfile import read_file
from gendiff.formaters.stylish_render import stylish_render
from gendiff.formaters.plain_render import plain_render
from gendiff.formaters.json_render import json_render


def generate_diff(path1, path2, formater_name='stylish'):
    """
    Generate a diff for a given files.
    Parameters:
        file_path1: A path to the first diff file.
        file_path2: A path to the second diff file.
        formater_name: Diff output format.
    Returns:
        Diff of the given files.
    """
    file1 = read_file(path1)
    file2 = read_file(path2)
    diff = make_diff(file1, file2)
    print_diff_in_selected_format = _select_formater(formater_name)
    return print_diff_in_selected_format(diff)


def _select_formater(name):
    """
    Select formater for specified output format
    Parameters:
        name: output format name
    Returns:
        function that makes specified output format
    """
    formaters = {
        'stylish': stylish_render,
        'plain': plain_render,
        'json': json_render
    }

    return formaters[name]
