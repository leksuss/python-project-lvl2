# coding=UTF-8

"""Main module with comparsing functions."""

from gendiff.scripts import io


def compare_nodes(node1, node2):
    diff = []
    for node1_key, node1_value in node1.items():
        if node1_key in node2:
            node2_value = node2.pop(node1_key)
            if type(node1_value) is dict and type(node2_value) is dict:
                node1_value = compare_nodes(node1_value, node2_value)
                diff.append({
                    'node_name': node1_key,
                    'node_value': node1_value,
                    'status': 'not_changed',
                })
            elif node1_value == node2_value:
                diff.append({
                    'node_name': node1_key,
                    'node_value': node1_value,
                    'status': 'not_changed',
                })
            else:
                diff.append({
                    'node_name': node1_key,
                    'node_value': {
                        'old': node1_value,
                        'new': node2_value,
                    },
                    'status': 'changed',
                })
        else:
            diff.append({
                'node_name': node1_key,
                'node_value': node1_value,
                'status': 'removed',
            })
    for new_key, new_value in node2.items():
        diff.append({
            'node_name': new_key,
            'node_value': new_value,
            'status': 'added',
        })
    return diff


def generate_diff(path_file1: str, path_file2: str) -> str:  # noqa: WPS210
    """Calculate difference between two dicts."""
    structure1 = io.read_file(path_file1)
    structure2 = io.read_file(path_file2)
    return compare_nodes(structure1, structure2)
