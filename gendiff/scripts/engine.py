# coding=UTF-8

"""Main module with comparsing functions."""

import json


def open_json(path_to_file: str) -> dict:
    """Read json file and return dict of it's content."""
    with open(path_to_file) as json_file:
        return json.load(json_file)


def generate_diff(path_file1: str, path_file2: str) -> str:  # noqa: WPS210
    """Calculate difference between two files."""
    diff = []
    file1 = open_json(path_file1)
    file2 = open_json(path_file2)
    for file1_key, file1_value in file1.items():
        file2_value = file2.pop(file1_key, False)
        if file2_value:
            if file2_value == file1_value:
                diff.append('   {0}: {1}'.format(file1_key, file1_value))
            else:
                diff.append(' + {0}: {1}'.format(file1_key, file2_value))
                diff.append(' - {0}: {1}'.format(file1_key, file1_value))
        else:
            diff.append(' - {0}: {1}'.format(file1_key, file1_value))
    for new_key, new_value in file2.items():
        diff.append(' + {0}: {1}'.format(new_key, new_value))
    return '{{\n{0}\n}}'.format('\n'.join(diff))
