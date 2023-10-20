import json


def main(file1, file2):
    file1, file2 = return_json(file1), return_json(file2)
    dictionary = merge(file1, file2)
    dictionary = dict(sorted(dictionary.items()))
    res = []
    for element in dictionary:
        if ele
            
        
    
        
        


def return_json(file):
    return json.load(open(f'gendiff.json-files.{file}'))


def merge(file1, file2):
    res = file1.copy()
    res.update(file2)
    return res


def flatten(dictionary):
    return [x for y in dictionary for x in y]
