import json
import yaml


def parse(file, ext):
    if ext == "json":
        return json.load(file)
    if ext == "yaml" or ext == "yml":
        return yaml.safe_load(file)
