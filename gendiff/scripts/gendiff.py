from gendiff import cli
from gendiff import generate_diff


def main():
    print(generate_diff(*cli.get_cli_args()))


if __name__ == '__main__':
    main()
