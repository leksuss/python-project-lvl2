# coding=UTF-8

"""Main module with comparsing functions."""

from gendiff.scripts import io


def compare_nodes(node1, node2):
    """Compare two nodes. Return list of dicts."""
    diff = []
    common_keys = node1.keys() | node2.keys()
    for key in common_keys:
        if key not in node1:
            node_value = node2[key]
            status = 'added'
        elif key not in node2:
            node_value = node1[key]
            status = 'removed'
        elif node1[key] == node2[key]:
            node_value = node1[key]
            status = 'unchanged'
        elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
            node_value = compare_nodes(node1[key], node2[key])
            status = 'unchanged'
        else:
            node_value = {'old': node1[key], 'new': node2[key]}
            status = 'changed'

        diff.append({
            'node_name': key,
            'node_value': node_value,
            'status': status,
        })
    return diff


def generate_diff(path_file1: str, path_file2: str) -> str:  # noqa: WPS210
    """Calculate difference between two dicts."""
    structure1 = io.read_file(path_file1)
    structure2 = io.read_file(path_file2)
    return compare_nodes(structure1, structure2)
