import json

# f = {
#   "host": "hexlet.io",
#   "timeout": 50,
#   "proxy": "123.234.53.22",
#   "follow": 'false'
# }

# s = {
#   "timeout": 20,
#   "verbose": 'true',
#   "host": "hexlet.io"
# }


def main(file1, file2):
    file1, file2 = json.load(open(file1)), json.load(open(file2))
    lst = []
    res = ''
    global value1
    global value2
    value1, value2 = list(file1.values()), list(file2.values())
    value1, value2 = list(map(str, value1)), list(map(str, value2))
    lst = create_list(file1, file2)

    lst = list(set(lst))
    lst = list(sorted(lst))

    lst = list(sorted(lst, key=sort_lst))

    res = build_string(lst)

    return f'{{\n{res}}}'


def create_list(file1, file2):
    temp = []
    for dicts in (file1, file2):
        for k, v in dicts.items():
            temp.append(f'{k}: {v}')
    return temp


def sort_lst(string):
    indx = string.find(' ')
    if str(string[indx + 1:]) in value1:
        return False
    else:
        return True


def build_string(res_list):
    res = ''
    for string in res_list:
        indx = string.find(' ')
        if str(string[indx + 1:] in value1 and str(string[indx + 1:])) in value2:  # noqa: E501
            res += f'    {string}\n'
            continue
        if str(string[indx + 1:]) in value1:
            res += f'  - {string}\n'
            continue
        if str(string[indx + 1:]) in value2:
            res += f'  + {string}\n'
            continue
    return res

# main(f, s)
