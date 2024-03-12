import os
from gendiff.consts import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED


def read_file(file):
    return open(file)


def get_extension(path):
    file_name = os.path.basename(path)
    _, ext = os.path.splitext(file_name)
    if ext == ".json":
        return "json"
    elif ext == ".yaml" or ext == ".yml":
        return "yaml"
    else:
        raise ValueError("Incorrect Extension")


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
