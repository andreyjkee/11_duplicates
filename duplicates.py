import argparse
import os
from collections import defaultdict


def build_files_dict(directory):
    name_size_to_paths = defaultdict(list)
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.exists(filepath):
                name_size_to_paths[os.path.basename(filepath) + ' ' + str(os.path.getsize(filepath))].append(filepath)
    return name_size_to_paths

def get_duplicates(directory):
    files_dict = build_files_dict(directory)
    return [val for val in files_dict.values() if len(val) > 1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get duplicated files")
    parser.add_argument("-d", "--dir", type=str, dest="directory", required=True)
    options = parser.parse_args()
    duplicates = get_duplicates(options.directory)
    if duplicates:
        print('Found duplicated files (by name and size):')
        for paths in duplicates:
            print(paths)
