import argparse


def get_cli_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
    )
    parser.add_argument(
        'first_file',
        type=str,
        default='',
        help='',
    )
    parser.add_argument(
        'second_file',
        type=str,
        default='',
        help='',
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='',
        help='set format of output',
    )
    args = parser.parse_args()
    return args.first_file, args.second_file
