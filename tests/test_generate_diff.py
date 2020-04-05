import pytest

from gendiff import generate_diff


@pytest.fixture
def expected_diff():
    return open('tests/fixtures/expected.txt').read()


def test_yaml_files(expected_diff):
    path_file1 = 'tests/fixtures/1.yaml'
    path_file2 = 'tests/fixtures/2.yaml'
    assert generate_diff(path_file1, path_file2) == expected_diff


def test_json_files(expected_diff):
    path_file1 = 'tests/fixtures/1.json'
    path_file2 = 'tests/fixtures/2.json'
    assert generate_diff(path_file1, path_file2) == expected_diff
