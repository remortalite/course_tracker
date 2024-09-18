import json


def load(path):
    with open(path, 'r') as f:
        data = json.loads(f.read())
    return data
