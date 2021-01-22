import os.path
import yaml


def read_file(file_path):
    """
    Read files with a given file names and return list of files structure.
    Parameters:
        file_path: The path to the file to read.
    Returns:
        File content, parsed to the dictionary.
    """
    absolute_path = os.path.abspath(file_path)
    file = open(absolute_path)
    return yaml.safe_load(file)
