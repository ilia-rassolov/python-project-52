import json


def parse_data(file_path, object):
    with open(file_path) as file:
        data = json.load(file)
    return data[object]