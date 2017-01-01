import os
from optparse import OptionParser


def are_files_duplicates(file_path_1, file_path_2):
    if not os.path.exists(file_path_1):
        raise FileNotFoundError(file_path_1)
    if not os.path.exists(file_path_2):
        raise FileNotFoundError(file_path_2)
    return all([os.path.getsize(file_path_1) == os.path.getsize(file_path_2),
                os.path.basename(file_path_1) == os.path.basename(file_path_2)])

def get_filepaths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.exists(filepath):
                file_paths.append(filepath)
    return file_paths


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--dir', type='string', dest='directory')
    (options, args) = parser.parse_args()
    duplicates = []
    all_files = get_filepaths(options.directory)
    list_of_pairs = [(all_files[p1], all_files[p2])
                     for p1 in range(len(all_files)) for p2 in range(p1 + 1, len(all_files))]
    for pair in list_of_pairs:
        if are_files_duplicates(*pair):
            duplicates.append(pair)
    if duplicates:
        print('Found duplicated files:')
        for dupe in duplicates:
            print('File 1: {0}, file 2: {1}'.format(dupe[0], dupe[1]))
