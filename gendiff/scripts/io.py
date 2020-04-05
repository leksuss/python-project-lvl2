# coding=UTF-8

"""Main module with comparsing functions."""

import json

import yaml


def read_json(path_to_file: str) -> dict:
    """Read json file and return dict of its content."""
    with open(path_to_file) as json_file:
        return json.load(json_file)


def read_yaml(path_to_file: str) -> dict:
    """Read yaml file and return dict of its content."""
    with open(path_to_file) as yaml_file:
        return yaml.load(yaml_file, Loader=yaml.SafeLoader)


def read_file(path_to_file: str):
    """Read file depending on its type and return content."""
    filetype = path_to_file.split('.')[-1]
    if filetype == 'json':
        read_func = read_json
    elif filetype == 'yaml':
        read_func = read_yaml
    return read_func(path_to_file)
