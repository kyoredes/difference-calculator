import os
from gendiff.scripts import generate_diff

current_dir = os.path.dirname(os.path.abspath(__file__))
path1 = f'{current_dir}/fixtures/file1.json'
path2 = f'{current_dir}/fixtures/file2.json'
correct = open(f'{current_dir}/fixtures/correct.txt').read()


def test_gendiff():
    assert generate_diff(path1, path2) == correct
