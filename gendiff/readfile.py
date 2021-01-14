import os.path
import yaml


def read_file(path):
    absolute_path = os.path.abspath(path)
    file = open(absolute_path)
    return yaml.safe_load(file)
