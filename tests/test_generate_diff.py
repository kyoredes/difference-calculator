from gendiff import generate_diff
import tests.fixtures as fixtures


def file1():
    return 'python-project-50/tests/fixtures/file1.json'


def file2():
    return 'python-project-50/tests/fixtures/file2.json'


def test_main():
    correct = "{\n- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}"  # noqa: E501
    assert generate_diff(file1(), file2()) == correct


# test_main(file1, file2)
# def test():
#    assert file1 == file2
