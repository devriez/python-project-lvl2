import os.path


def read_json_file(path):
    absolute_path = os.path.abspath(path)
    return json.load(open(absolute_path))
