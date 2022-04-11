import os
import json as js

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        data = js.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]


def linear_search(sequence, our_number):
    vystup = {"positions": [], "count": 0}
    for idx, number in enumerate(sequence):
        if number == our_number:
            vystup["positions"].append(idx)
            vystup["count"] += 1
    return vystup


def pattern_search(sequence, string):
    positions = set()
    for idx, subdata in enumerate(sequence):
        if idx + len(string ) < len(sequence):
            if sequence[idx:idx + len(string)] == string:
                positions.add(idx)
    return positions



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(linear_search(sequential_data, 5))
    file_path = os.path.join(cwd_path, "sequential.json")
    with open(file_path, "r") as json_file:
        sequence = js.load(json_file)["dna_sequence"]
    print(pattern_search(sequence, "ATA"))

if __name__ == '__main__':
    main()