import os
from gendiff import generate_diff

current_dir = os.path.dirname(os.path.abspath(__file__))
path1 = f'{current_dir}/fixtures/tree_file1.json'
path2 = f'{current_dir}/fixtures/tree_file2.json'
correct = open(f'{current_dir}/fixtures/correct.txt').read()


print(generate_diff(path1, path2))
