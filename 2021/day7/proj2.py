#!/usr/bin/env python

import proj1


def gas_usage(steps):
    """Find the total gas usage from the steps taken"""
    return int(steps * steps / 2 + steps / 2)


def find_min_gas_updated_fuel_usage(data):
    """Turns our you're a dumb bish and need to refactor how you determine what the lowest gas usage is. For every step
    our crabs take, they use an incremental amount of gas:
     1 step = 1 gas
     2 steps = 1 + 2 gas
     3 steps = 1 + 2 + 3 gas"""
    lowest_diff = None
    for meet_up_num in data:
        differences = list()
        for num in data:
            fuel = gas_usage(abs(num - meet_up_num))
            differences.append(fuel)
        sum_to_test = sum(differences)
        if not lowest_diff or sum_to_test < lowest_diff:
            lowest_diff = sum_to_test
    return lowest_diff


if __name__ == '__main__':
    data_file = 'crabs.txt'
    data = proj1.get_data(data_file)
    lowest = find_min_gas_updated_fuel_usage(data)
    print(lowest)
