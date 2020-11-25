# coding=UTF-8

"""Main module with comparsing functions."""

from gendiff.scripts import io
from pprint import pprint


def add_record(array, node_name, node_value, status):
    array.append({
        'node_name': node_name,
        'node_value': node_value,
        'status': status,
    })
    return array


def compare_nodes(node1, node2):
    diff = []
    common_keys = node1.keys() | node2.keys()
    for key in common_keys:
        if key not in node1:
            diff = add_record(diff, key, node2[key], 'added')
        elif key not in node2:
            diff = add_record(diff, key, node1[key], 'removed')
        elif node1[key] == node2[key]:
            diff = add_record(diff, key, node1[key], 'unchanged')
        elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
            node1[key] = compare_nodes(node1[key], node2[key])
            diff = add_record(diff, key, node1[key], 'unchanged')
        else:
            diff = add_record(diff, key, {
                'old': node1[key],
                'new': node2[key],
            }, 'changed')
    return diff


def generate_diff(path_file1: str, path_file2: str) -> str:  # noqa: WPS210
    """Calculate difference between two dicts."""
    structure1 = io.read_file(path_file1)
    structure2 = io.read_file(path_file2)
    return compare_nodes(structure1, structure2)
