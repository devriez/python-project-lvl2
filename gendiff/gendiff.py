from gendiff.makediff import make_diff
from gendiff.selectformater import select_formater
from gendiff.readfile import read_file


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
    formater = select_formater(formater_name)
    return formater(diff)