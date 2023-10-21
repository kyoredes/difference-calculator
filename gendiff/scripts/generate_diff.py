import json


def main(file1, file2):
    file1, file2 = return_json(file1), return_json(file2)
    # file1 = '-'
    # file2 = '+'
    value1, value2 = list(file1.values()), list(file2.values())
    res = ''
    dictionary = merge(file1, file2)
    dictionary = dict(sorted(dictionary.items()))
    for key in dictionary:
        # only value1
        if dictionary[key] in value1 and dictionary[key] not in value2:
            res += f'   - {key}: {dictionary[key]}\n'
            continue
        # only value2
        if dictionary[key] in value2 and dictionary[key] not in value1:
            res += f'   + {key}: {dictionary[key]}\n'
            continue
        if dictionary[key] in value1 and dictionary[key] in value2:
            res += f'   {key}: {dictionary[key]}\n'
            continue
    return f'{{\n{res}\n}}'


def return_json(file):
    return json.load(open(f'gendiff.json-files.{file}'))


def merge(file1, file2):
    res = file1.copy()
    res.update(file2)
    return res
