from gendiff.generate_diff import generate_diff  # noqa E:501
from gendiff.formatters.stylish import build_string, replace_bool  # noqa E:501
from gendiff.formatters.plain import build_plain  # noqa E:501
from gendiff.formatters.json_format import build_json  # noqa E:501
from gendiff.parse_file import parse
from gendiff.generate_diff import get_extension, read_file


def main(file1, file2, format_name='stylish'):
    f1, f2 = parse(read_file(file1), get_extension(file1)), parse(read_file(file2), get_extension(file2))  # noqa E:501
    diff = generate_diff(f1, f2)
    if format_name == 'stylish':
        res_str = build_string(diff)
    elif format_name == 'plain':
        res_str = build_plain(diff)
    elif format_name == 'json':
        res_str = build_json(diff)
    else:
        raise NameError('Unknown format name')
    res_str = replace_bool(res_str)
    return res_str
