import json


def generate_diff(path_to_file1, path_to_file2):
    difference = ''
    content_file1 = json.load(open(path_to_file1))
    content_file2 = json.load(open(path_to_file2))
    for file1_key, file1_value in content_file1.items():
        file2_value = content_file2.pop(file1_key, False)
        if file2_value:
            if file2_value == file1_value:
                difference += '   {0}: {1}\n'.format(file1_key, file1_value)
            else:
                difference += ' + {0}: {1}\n'.format(file1_key, file2_value)
                difference += ' - {0}: {1}\n'.format(file1_key, file1_value)
        else:
            difference += ' - {0}: {1}\n'.format(file1_key, file1_value)
    for file2_key, file2_value in content_file2.items():
        difference += ' + {0}: {1}\n'.format(file2_key, file2_value)
    return '{{\n{0}}}'.format(difference)
