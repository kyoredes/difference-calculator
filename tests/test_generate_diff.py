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
    correct = "{\n- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}"  # noqa: E501
    assert generate_diff(file1, file2) == correct
