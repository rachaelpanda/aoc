#!/usr/bin/env python

import proj1


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



def determine_oxy_co2_rates(bit_count_dict, diagnostics):
    """Cycle through our diagnostics list and compare the most and least common bits. Keep only the diagnositcs that
    match our bit criteria for the type of rating.

    Oxygen generator rating is determined by the most common bit. If 0 and 1 are equally common, default to 1.
    CO2 scrubber rating is the least common bit for that placement. If 0 and 1 are equal, default to 0.

    Once we have one binary number left for that rating, you're done parsing for that rating."""
    pass


def deteremine_life_support_rating(a, b):
    pass


if __name__ == '__main__':
    diag_file = 'diagnostic_report.txt'
    diagnostics = proj1.get_diagnositcs(diag_file)
    #bit_count_dict = proj1.determine_common_bits(diagnostics)
