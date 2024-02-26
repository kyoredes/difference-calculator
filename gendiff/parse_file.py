import json
import yaml
import os


def read_file(file):
    file_name = os.path.basename(file)
    _, file_ext = os.path.splitext(file_name)
    if file_ext == ".json":
        res = json.load(open(file))
    elif file_ext == ".yaml" or file_ext == ".yml":  # noqa E:501
        res = yaml.safe_load(open(file))
    return res
