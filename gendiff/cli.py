# coding=UTF-8

"""Module to working with cli arguments."""

import argparse
from pprint import pprint


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
        default='plain',
        help='set format of output',
    )
    return parser.parse_args()


def print_result_of(difference: str) -> None:
    """Print difference of two files."""
    pprint(difference)
