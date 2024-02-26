import os
from gendiff import generate_diff
import pytest


current_dir = os.path.dirname(os.path.abspath(__file__))
json_path1 = f'{current_dir}/fixtures/file1.json'
json_path2 = f'{current_dir}/fixtures/file2.json'

correct = open(f'{current_dir}/fixtures/correct.txt').read()
tree_correct = open(f'{current_dir}/fixtures/correct_tree.txt').read()
correct_plain = open(f'{current_dir}/fixtures/correct_plain.txt').read()
correct_json = open(f'{current_dir}/fixtures/correct_json.txt').read()

yaml_path1 = f'{current_dir}/fixtures/file1.yaml'
yaml_path2 = f'{current_dir}/fixtures/file2.yaml'

json_tree1 = f'{current_dir}/fixtures/tree_file1.json'
json_tree2 = f'{current_dir}/fixtures/tree_file2.json'

yaml_tree1 = f'{current_dir}/fixtures/tree_file1.yaml'
yaml_tree2 = f'{current_dir}/fixtures/tree_file2.yaml'


@pytest.mark.parametrize("file1, file2, format_name,     expected", [
    (json_path1, json_path2, 'stylish', correct),
    (json_tree1, json_tree2, 'stylish', tree_correct),
    (yaml_path1, yaml_path2, 'stylish', correct),
    (yaml_tree1, yaml_tree2, 'stylish', tree_correct),
    (json_tree1, json_tree2, 'plain', correct_plain),
    (json_tree1, json_tree2, 'json', correct_json)])
def test_gendiff(file1, file2, format_name, expected):
    result = generate_diff(file1, file2, format_name)
    assert result.rstrip() == expected.rstrip()
