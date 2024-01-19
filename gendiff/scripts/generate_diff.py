import json
import yaml
import os


def main(file1, file2):
    file1, file2 = read_file(file1, file2)
    lst = []
    res = ''
    global value1
    global value2
    value1, value2 = list(file1.values()), list(file2.values())  # переводим !!!значения!!! (из пары ключ-значения) json-файлов в два списка # noqa: E501
    value1, value2 = list(map(str, value1)), list(map(str, value2))  # преобразуем все !!!значения!!! списков в строковые # noqa: E501
    lst = create_list(file1, file2)  # сливаем оба файла в один список строк "ключ: значение" . сейчас они не отсортированы и дубликаты не удалены # noqa: E501
    # lst = clean_dict(lst)

    lst = list(set(lst))
    lst = list(sorted(lst))

    lst = list(sorted(lst, key=sort_lst))  # сортируем по дифу (какой файл с каким сравниаем) # noqa: E501

    res = build_string(lst)
    res = replace_bool(res)

    return f'{{\n{res}}}'


def read_file(file1, file2):
    file1_name = os.path.basename(file1)
    file2_name = os.path.basename(file2)
    _, file1_ext = os.path.splitext(file1_name)
    _, file2_ext = os.path.splitext(file2_name)
    if file1_ext == file2_ext:
        if file1_ext == "yaml":
            res1 = yaml.load(open(file1))
            res2 = yaml.load(open(file2))
            return res1, res2
        else:
            res1 = json.load(open(file1))
            res2 = json.load(open(file2))
            return res1, res2
    else:
        if file1_ext == "yaml":
            res1 = yaml.load(open(file1))
            res2 = json.load(open(file2))
            return res1, res2
        else:
            res1 = json.load(open(file1))
            res2 = yaml.load(open(file2))
            return res1, res2


# f1 = {
#   "common": {
#     "setting1": "Value 1",
#     "setting2": 200,
#     "setting3": 'true',
#     "setting6": {
#       "key": "value",
#       "doge": {
#         "wow": ""
#       }
#     }
#   },
#   "group1": {
#     "baz": "bas",
#     "foo": "bar",
#     "nest": {
#       "key": "value"
#     }
#   },
#   "group2": {
#     "abc": 12345,
#     "deep": {
#       "id": 45
#     }
#   }
# }

# f2 = {
#   "common": {
#     "follow": 'false',
#     "setting1": "Value 1",
#     "setting3": 'null',
#     "setting4": "blah blah",
#     "setting5": {
#       "key5": "value5"
#     },
#     "setting6": {
#       "key": "value",
#       "ops": "vops",
#       "doge": {
#         "wow": "so much"
#       }
#     }
#   },
#   "group1": {
#     "foo": "bar",
#     "baz": "bars",
#     "nest": "str"
#   },
#   "group3": {
#     "deep": {
#       "id": {
#         "number": 45
#       }
#     },
#     "fee": 100500
#   }
# }


def extract_values(dictionary):
    values = []
    for value in dictionary.values():
        if isinstance(value, dict):
            values.extend(extract_values(value))
        else:
            values.append(value)
    return values


global value1
global value2

value1 = extract_values(f1)
value2 = extract_values(f2)


def merge_dicts_to_list(*files, result=[], indx=None):
    for d in files:
        for k, v in d.items():
            flag = False
            if isinstance(v, dict):
                result.append(k)
                result.append([])
                indx = result.index([])
                merge_dicts_to_list(v, indx=indx)
            if indx != None:
                result[indx].append(f'{k}: {v}')
        return result


lst = unite_dicts(f1, f2)


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def get_value_nested_level(dictionary, k, target_value, level=0):
    for value in dictionary.values():
        if value == target_value and get_key(dictionary, value) == k:
            return level
        elif isinstance(value, dict):
            nested_level = get_value_nested_level(value, k, target_value, level + 1)  # noqa: E501
            if nested_level is not None:
                return nested_level
    return None


def get_key_nested_level(dictionary, k, level=0):
    for key, value in dictionary.items():
        if key == k:
            return level
        elif isinstance(value, dict):
            nested_level = get_key_nested_level(value, k, level + 1)
            if nested_level is not None:
                return nested_level
    return None


# num_value = get_value_nested_level(f1, 'setting2', 200)
# print(num_value)
# num_key = get_key_nested_level(f1, 'key')
# print(num_key)


# def build_string(res_list):
#     res = ''
#     for string in res_list:
#         indx = string.find(' ')
#         if str(string[indx + 1:] in value1 and str(string[indx + 1:])) in value2:  # noqa: E501
#             res += f'    {string}\n'
#             continue
#         if str(string[indx + 1:]) in value1:
#             res += f'  - {string}\n'
#             continue
#         if str(string[indx + 1:]) in value2:
#             res += f'  + {string}\n'
#             continue
#     return res


# s = build_string(lst)
# print(s)



# def replace_bool(string):
#     string = string.replace('True', 'true')
#     string = string.replace('False', 'false')
#     return string


# main(f, s)
