import os.path
import json
import yaml


def read_file(path):
    absolute_path = os.path.abspath(path)
    file = open(absolute_path)
    #return json.load()
    return yaml.load(file)
