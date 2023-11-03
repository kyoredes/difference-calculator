from gendiff.scripts import generate_diff
from tests.fixtures import file1
from tests.fixtures import file2
from tests.fixtures import correct

def test_gendiff():
    assert generate_diff(file1, file2) == correct
