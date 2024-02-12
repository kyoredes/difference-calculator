import os
from gendiff import generate_diff

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path1 = f'{current_dir}/fixtures/file1.json'
json_path2 = f'{current_dir}/fixtures/file2.json'
correct = open(f'{current_dir}/fixtures/correct.txt').read()

yaml_path1 = f'{current_dir}/fixtures/file1.yaml'
yaml_path2 = f'{current_dir}/fixtures/file2.yaml'


def test_json_gendiff():
    assert generate_diff(json_path1, json_path2) == correct


def test_yaml_gendiff():
    assert generate_diff(yaml_path1, yaml_path2) == correct
