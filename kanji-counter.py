"""
kanji-counter.py

Package kanji-counter

Author:
    kinami

Created:
    14/4/22
"""

import json


# Reads the json file and returns a dictionary
def read_json(file_name):
    with open(file_name) as f:
        return json.load(f)


# Groups the kanji by the value of the key inputted
def group_by(dictionary, key):
    return {k: len([i for i in dictionary.values() if i[key] == k]) for k in set([i[key] for i in dictionary.values()])}


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print('Usage: kanji-counter.py <json file> <current level>')
        sys.exit(1)
    entries = read_json(sys.argv[1])
    grouped = group_by(entries, 'wk_level')
    print(f'Learned {sum([grouped[i] for i in grouped.keys() if i is not None and i <= int(sys.argv[2])])} kanji')
