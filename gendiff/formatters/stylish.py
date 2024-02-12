import json
from gendiff.consts import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED


def change_bool(value):
    if isinstance(value, bool) or value is None:
        return str(value).lower()
    return value


def unpack_value(d):
    res = {}
    for k, v in d.items():
        if isinstance(v, dict):
            res[k] = unpack_value(v)
        res[f"  {k}"] = change_bool(v)
    return res


def build_dict(data):  # noqa
    res = {}
    for k, v in data.items():
        if v['type'] == NESTED:
            res[f"{k}"] = build_dict(v['value'])

        elif v['type'] == ADDED:
            res[f"+ {k}"] = change_bool(v['value'])

        elif v['type'] == REMOVED:
            res[f"- {k}"] = change_bool(v['value'])

        elif v['type'] == CHANGED:
            if isinstance(v['old_value'], dict):
                res[f"- {k}"] = unpack_value(v['old_value'])  # noqa E:501
            else:
                res[f"- {k}"] = change_bool(v['old_value'])
            if isinstance(v['new_value'], dict):
                res[f"+ {k}"] = unpack_value(v['new_value'])  # noqa E:501
            else:
                res[f"+ {k}"] = change_bool(v['new_value'])

        elif v['type'] == UNCHANGED:
            res[f"  {k}"] = change_bool(v['value'])

    return res


def build_string(res_dict):
    x = res_dict
    xstr = json.dumps(x, indent=4)
    xstr = xstr.replace('"', "")
    xstr = xstr.replace(",", "")
    return xstr
