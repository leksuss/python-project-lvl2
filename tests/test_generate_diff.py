import pytest

from gendiff import generate_diff


@pytest.fixture
def expected_diff():
    return open('tests/fixtures/simple_diff_expected.txt').read()

'''
def test_simple_yaml_files(expected_diff):
    path_file1 = 'tests/fixtures/simple_1.yaml'
    path_file2 = 'tests/fixtures/simple_2.yaml'
    assert generate_diff(path_file1, path_file2) == expected_diff


def test_simple_json_files(expected_diff):
    path_file1 = 'tests/fixtures/simple_1.json'
    path_file2 = 'tests/fixtures/simple_2.json'
    assert generate_diff(path_file1, path_file2) == expected_diff
'''

@pytest.fixture
def expected_diff():
    from tests.fixtures.test_expected import expected
    return expected


def test_simple_json_files(expected_diff):
    path_file1 = 'tests/fixtures/test1.json'
    path_file2 = 'tests/fixtures/test2.json'
    assert generate_diff(path_file1, path_file2) == expected_diff