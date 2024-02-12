from gendiff.scripts.generate_diff import read_file, generate_diff  # noqa E:501
from gendiff.formatters.stylish import unpack_value, build_dict, build_string  # noqa E:501


def main(file1, file2):
    f1, f2 = read_file(file1, file2)
    diff = generate_diff(f1, f2)
    res_dict = build_dict(diff)
    res_str = build_string(res_dict)
    return res_str
