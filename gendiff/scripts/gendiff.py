import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',  help='set format of output')  # noqa E501
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
