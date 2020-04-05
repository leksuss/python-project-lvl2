# coding=UTF-8

"""Module to excecute program running from cli."""

from gendiff import cli, generate_diff


def main() -> None:
    """Get and return to cli result of comparing two files."""
    args = cli.get_cli_args()
    cli.print_result_of(generate_diff(
        args.first_file,
        args.second_file,
    ))


if __name__ == '__main__':
    main()
