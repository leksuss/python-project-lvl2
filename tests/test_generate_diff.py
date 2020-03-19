from gendiff import generate_diff


def test_generate_diff():
    path_file1 = 'tests/fixtures/1.json'
    path_file2 = 'tests/fixtures/2.json'
    expected_diff = open('tests/fixtures/expected.txt').read()
    assert generate_diff(path_file1, path_file2) == expected_diff
