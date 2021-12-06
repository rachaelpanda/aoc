#!/usr/bin/env python


def get_diagnositcs(diag_file):
    """Grab the diagnostics from text file and clean it up"""
    with open(diag_file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def determine_common_bits(diagnostics):
    """Given our diagnostics in binary, parse for the common and uncommon bits in each row. Return a dictionary
    containing a bit count for each row"""
    # create our dictionary to track the count of 0's and 1's for each row
    bit_counts = dict()
    for i in range(len(diagnostics[0])):
        bit_counts.update({i: {'0': 0, '1': 0}})
    for binary_str in diagnostics:
        # break down our string into a list to iterate through
        binary_list = list(binary_str)
        # loop through the list and update the bit_count dict with each row's value
        for index in range(len(binary_list)):
            bit_counts[index][str(binary_list[index])] += 1
    return bit_counts


def get_decimal(binary):
    """Given a binary number, return the decimal"""
    return int(binary, 2)


def get_gamma_epsilon_rates(bit_count_dict, gamma='', epsilon=''):
    """Iterate through the bit count dictionary to determine the most and least common bits used. The most common bits
    are a part of the gamma rate and the least common bit is the epsilon rate. Return """
    # Determine most and least common bits used
    for i in bit_count_dict:
        if bit_count_dict[i]['0'] > bit_count_dict[i]['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    gamma = get_decimal(gamma)
    epsilon = get_decimal(epsilon)
    return gamma, epsilon


def print_product(a, b):
    """Print the product of two numbers."""
    product = a * b
    print(product)


if __name__ == '__main__':
    diag_file = 'diagnostic_report.txt'
    diagnostics = get_diagnositcs(diag_file)
    bit_count_dict = determine_common_bits(diagnostics)
    gamma, epsilon = get_gamma_epsilon_rates(bit_count_dict)
    print('The power consumption is:')
    print_product(gamma, epsilon)
