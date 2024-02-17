from gendiff.scripts.generate_diff import read_file, generate_diff  # noqa E:501
from gendiff.formatters.stylish import unpack_value, build_string, replace_bool  # noqa E:501


def main(file1, file2):
    f1, f2 = read_file(file1, file2)
    diff = generate_diff(f1, f2)
    res_str = build_string(diff)
    res_str = replace_bool(res_str)
    return res_str
