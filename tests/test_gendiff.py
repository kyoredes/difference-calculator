import os
from gendiff import generate_diff

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path1 = f'{current_dir}/fixtures/file1.json'
json_path2 = f'{current_dir}/fixtures/file2.json'

correct = open(f'{current_dir}/fixtures/correct.txt').read()
tree_correct = open(f'{current_dir}/fixtures/correct_tree.txt').read()
correct_plain = open(f'{current_dir}/fixtures/correct_plain.txt').read()

yaml_path1 = f'{current_dir}/fixtures/file1.yaml'
yaml_path2 = f'{current_dir}/fixtures/file2.yaml'

json_tree1 = f'{current_dir}/fixtures/tree_file1.json'
json_tree2 = f'{current_dir}/fixtures/tree_file2.json'

yaml_tree1 = f'{current_dir}/fixtures/tree_file1.yaml'
yaml_tree2 = f'{current_dir}/fixtures/tree_file2.yaml'


def test_json_gendiff():
    assert generate_diff(json_path1, json_path2).rstrip() == correct.rstrip()
    assert generate_diff(json_tree1, json_tree2).rstrip() == tree_correct.rstrip()  # noqa E:501


def test_yaml_gendiff():
    assert generate_diff(yaml_path1, yaml_path2).rstrip() == correct.rstrip()
    assert generate_diff(yaml_tree1, yaml_tree2).rstrip() == tree_correct.rstrip()  # noqa E:501


def test_plain_gendiff():
    assert generate_diff(json_tree1, json_tree2, format_name='plain').rstrip() == correct_plain.rstrip()  # noqa E:501
