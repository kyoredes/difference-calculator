from gendiff.scripts.generate_diff import read_file, generate_diff  # noqa E:501
from gendiff.formatters.stylish import build_string, replace_bool  # noqa E:501
from gendiff.formatters.plain import build_plain  # noqa E:501


class FormatError(Exception):
    pass


def main(file1, file2, format_name='stylish'):
    f1, f2 = read_file(file1, file2)
    diff = main(f1, f2)
    if format_name == 'stylish':
        res_str = build_string(diff)
    elif format_name == 'plain':
        res_str = build_plain(diff)
    else:
        raise FormatError('Unknown format name')
    res_str = replace_bool(res_str)
    return res_str
