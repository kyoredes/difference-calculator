import json


def main(file1, file2):
    file1, file2 = return_json(file1), return_json(file2)
    file1, file2 = dict(sorted(file1.items())), dict(sorted(file2.items()))
    dictionary = merge(file1, file2)
    res = ''
    for element in dictionary:
        
    
        
        


def return_json(file):
    return json.load(open(f'gendiff.json-files.{file}'))


def merge(file1, file2):
    res = file1.copy()
    res.update(file2)
    return res

