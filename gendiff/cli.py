# coding=UTF-8

"""Module to working with cli arguments."""

import argparse


def get_cli_args() -> tuple:
    """Parse args from cli to get path's to files we compare."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
    )
    parser.add_argument(
        'first_file',
        type=str,
    )
    parser.add_argument(
        'second_file',
        type=str,
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='json',
        help='set format of output',
    )
    args = parser.parse_args()
    return args.first_file, args.second_file


def print_result_of(difference: str) -> None:
    """Print difference of two files."""
    print(difference)
