#!/usr/bin/env python


def get_data(data_file):
    """Grab the data from text file and clean it up"""
    with open(data_file) as f:
        data = f.read()
    data = [int(num) for num in data.split(',')]
    data.sort()
    return data


def find_min_gas(data):
    """Get the absolute value from each number subtracted by every number within our data set to find the most fuel
    efficient meeting point for our cRaBs"""
    # brute force method idk what else to use
    lowest_diff = None
    for meet_up_num in data:
        differences = list()
        for num in data:
            differences.append(abs(num - meet_up_num))
        sum_to_test = sum(differences)
        if not lowest_diff or sum_to_test < lowest_diff:
            lowest_diff = sum_to_test
    return lowest_diff


if __name__ == '__main__':
    data_file = 'crabs.txt'
    data = get_data(data_file)
    lowest_diff = find_min_gas(data)
    print(lowest_diff)
