import json
from gendiff.consts import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED

def unpack_value(elmnt, level=0):
    res = []
    tabs = '    ' * level
    if not isinstance(elmnt, dict):
        return elmnt
    for k, v in elmnt.items():
        res.append(f'{tabs}    {k}: {unpack_value(v, level+1)}')
    return '{\n' + '\n'.join(res) + '\n' + tabs + '}'


def build_string(data, level=1):  # noqa
    res = []
    tabs = ' ' * (4 * level - 4)
    for k, v in data.items():

        if v['type'] == 'nested':
            res.append(f'{tabs}    {k}: {build_string(v["value"],  level+1)}')

        elif v['type'] == 'added':
            res.append(f'{tabs}  + {k}: {unpack_value(v["value"], level)}')

        elif v['type'] == 'removed':
            res.append(f'{tabs}  - {k}: {unpack_value(v["value"], level)}')

        elif v['type'] == 'changed':
            res.append(f'{tabs}  - {k}: {unpack_value(v["old_value"], level)}')
            res.append(f'{tabs}  + {k}: {unpack_value(v["new_value"], level)}')

        elif v['type'] == 'unchanged':
            res.append(f'{tabs}    {k}: {unpack_value(v["value"], level)}')

    return '{\n' + '\n'.join(res) + '\n' + tabs + '}'


def replace_bool(data):
    xstr = data
    xstr = xstr.replace('False', 'false')
    xstr = xstr.replace('True', 'true')
    xstr = xstr.replace('None', 'null')
    return xstr

