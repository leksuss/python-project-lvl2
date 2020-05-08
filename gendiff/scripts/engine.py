# coding=UTF-8

"""Main module with comparsing functions."""

from gendiff.scripts import io


def comparsion(file1, file2):
    diff = []
    for file1_key, file1_value in file1.items():
        file2_value = file2.pop(file1_key, False)
        if file2_value:
            if file2_value == file1_value:
                diff.append({
                    'node_name': file1_key,
                    'node_value': file1_value,
                })
            else:
                diff.append({
                    'node_name': file1_key,
                    'node_value': {
                        'old': file1_value,
                        'new': file2_value,
                    },
                })
        else:
            diff.append({
                'node_name': file1_key,
                'node_value': {
                    'old': file1_value,
                    'new': '',
                },
            })
    for new_key, new_value in file2.items():
        diff.append({
            'node_name': new_key,
            'node_value': {
                'old': '',
                'new': new_value,
            },
        })
    return diff


def generate_diff(path_file1: str, path_file2: str) -> str:  # noqa: WPS210
    """Calculate difference between two dicts."""
    structure1 = io.read_file(path_file1)
    structure2 = io.read_file(path_file2)
    return comparsion(structure1, structure2)


