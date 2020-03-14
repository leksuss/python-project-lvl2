# coding=UTF-8

"""Module to excecute program running from cli."""

from gendiff import cli, generate_diff


def main() -> None:
    """Get and return to cli result of comparing two files."""
    cli.print_result_of(generate_diff(*cli.get_cli_args()))


if __name__ == '__main__':
    main()
