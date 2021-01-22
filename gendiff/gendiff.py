from gendiff.makediff import make_diff
from gendiff.selectformater import select_formater
from gendiff.readfile import read_file


def generate_diff(path1, path2, formater_name='stylish'):
    file1 = read_file(path1)
    file2 = read_file(path2)
    diff = make_diff(file1, file2)
    formater = select_formater(formater_name)
    return formater(diff)