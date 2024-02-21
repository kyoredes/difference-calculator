import json
import yaml
import os
from gendiff.consts import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED


def read_file(file):
    file_name = os.path.basename(file)
    _, file_ext = os.path.splitext(file_name)
    if file_ext == ".json":
        res = json.load(open(file))
    elif file_ext == ".yaml" or file_ext == ".yml":  # noqa E:501
        res = yaml.safe_load(open(file))
    return res


def generate_diff(before: dict, after: dict) -> dict:  # noqa
    all_keys = before.keys() | after.keys()
    all_keys = sorted(all_keys)
    diff = {}
    for key in all_keys:

        if key not in after:
            # key был удален.
            diff[key] = {"type": REMOVED, "value": before[key]}

        if key not in before:
            # key был добавлен
            diff[key] = {"type": ADDED, "value": after[key]}

        if key in before and key in after:
            if isinstance(before[key], dict) and isinstance(after[key], dict):
                diff[key] = {"type": NESTED, "value": generate_diff(before[key], after[key])}  # noqa
                continue

            if before[key] != after[key]:
                diff[key] = {"type": CHANGED, "old_value": before[key], "new_value": after[key]}  # noqa
            else:
                diff[key] = {"type": UNCHANGED, "value": before[key]}
    return diff
