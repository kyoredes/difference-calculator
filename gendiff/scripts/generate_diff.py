import json
import yaml
import os

ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
NESTED = "nested"

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


def generate_diff(before: dict, after: dict) -> dict:
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
