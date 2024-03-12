import os
from gendiff import gendiff
import pytest


# json_path1 = f'{current_dir}/fixtures/file1.json'
# json_path2 = f'{current_dir}/fixtures/file2.json'

# correct = open(f'{current_dir}/fixtures/correct.txt').read()
# tree_correct = open(f'{current_dir}/fixtures/correct_tree.txt').read()
# correct_plain = open(f'{current_dir}/fixtures/correct_plain.txt').read()
# correct_json = open(f'{current_dir}/fixtures/correct_json.txt').read()

# yaml_path1 = f'{current_dir}/fixtures/file1.yaml'
# yaml_path2 = f'{current_dir}/fixtures/file2.yaml'

# json_tree1 = f'{current_dir}/fixtures/tree_file1.json'
# json_tree2 = f'{current_dir}/fixtures/tree_file2.json'

# yaml_tree1 = f'{current_dir}/fixtures/tree_file1.yaml'
# yaml_tree2 = f'{current_dir}/fixtures/tree_file2.yaml'


@pytest.mark.parametrize("path1, path2, format_name, expected", [
    ('/fixtures/file1.json', '/fixtures/file2.json', 'stylish', '/fixtures/correct.txt'),  # noqa E:501
    ('/fixtures/tree_file1.json', '/fixtures/tree_file2.json', 'stylish', '/fixtures/correct_tree.txt'),  # noqa E:501
    ('/fixtures/file1.yaml', '/fixtures/file2.yaml', 'stylish', '/fixtures/correct.txt'),  # noqa E:501
    ('/fixtures/tree_file1.yaml', '/fixtures/tree_file2.yaml', 'stylish', '/fixtures/correct_tree.txt'),  # noqa E:501
    ('/fixtures/tree_file1.json', '/fixtures/tree_file2.json', 'plain', '/fixtures/correct_plain.txt'),  # noqa E:501
    ('/fixtures/tree_file1.json', '/fixtures/tree_file2.json', 'json', '/fixtures/correct_json.txt')])  # noqa E:501
def test_gendiff(path1, path2, format_name, expected):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file1 = f'{current_dir}{path1}'
    file2 = f'{current_dir}{path2}'
    result = gendiff(file1, file2, format_name)
    expected = open(f'{current_dir}{expected}').read()
    assert result.rstrip() == expected.rstrip()
