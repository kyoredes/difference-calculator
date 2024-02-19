import os
from gendiff import generate_diff

current_dir = os.path.dirname(os.path.abspath(__file__))
path1 = f'{current_dir}/fixtures/tree_file1.json'
path2 = f'{current_dir}/fixtures/tree_file2.json'
correct = open(f'{current_dir}/fixtures/correct.txt').read()

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path1 = f'{current_dir}/fixtures/file1.json'
json_path2 = f'{current_dir}/fixtures/file2.json'

correct = open(f'{current_dir}/fixtures/correct.txt').read()
tree_correct = open(f'{current_dir}/fixtures/correct_tree.txt').read()

yaml_path1 = f'{current_dir}/fixtures/file1.yaml'
yaml_path2 = f'{current_dir}/fixtures/file2.yaml'

json_tree1 = f'{current_dir}/fixtures/tree_file1.json'
json_tree2 = f'{current_dir}/fixtures/tree_file2.json'

yaml_tree1 = f'{current_dir}/fixtures/tree_file1.yaml'
yaml_tree2 = f'{current_dir}/fixtures/tree_file2.yaml'


print(generate_diff(json_tree1, json_tree2, format_name='json'))
