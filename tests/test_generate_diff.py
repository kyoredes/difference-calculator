# import pytest
from gendiff.scripts.generate_diff import main
import tests.fixtures as fixtures


# @pytest.fixture
def file1():
    return fixtures.file1


# @pytest.fixture
def file2():
    pass

print(file1)