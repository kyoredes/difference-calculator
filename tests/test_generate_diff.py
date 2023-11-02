import pytest
import json
from gendiff import generate_diff
import tests.fixtures as fixtures


@pytest.fixture
def file1():
    return json.load(open(fixtures.file1))


@pytest.fixture
def file2():
    return json.load(open(fixtures.file2))


def test_main(file1, file2):
    correct = '{
    - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'

