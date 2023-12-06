#!/usr/bin/env python3

# import re

def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def concat(a, b):
    return int(f"{a}{b}")


def get_numbers(lines):
    # dang number clashing! oneight, threeight, eightwo, etc
    conversion_dict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
        "zero": "z0o",
    }
    total_numbers = list()
    for line in lines:
        translatedLine = line
        for key, value in conversion_dict.items():
            translatedLine = translatedLine.replace(key, value)
        numbers_line = [int(i) for i in list(translatedLine) if i.isdigit()]
        if len(numbers_line) > 1:
            first_and_last = numbers_line[::len(numbers_line) - 1]
            final_number = int("".join(map(str, first_and_last)))
        else:
            final_number = concat(numbers_line[0], numbers_line[0])
        total_numbers.append(final_number)
    return total_numbers


# def convert_to_int(list_to_convert):
#     number_converter = {
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#         'one': 1,
#         'two': 2,
#         'three': 3,
#         'four': 4,
#         'five': 5,
#         'six': 6,
#         'seven': 7,
#         'eight': 8,
#         'nine': 9
#     }
#     converted_list = list()
#     for i in list_to_convert:
#         converted_list.append(number_converter[i])
#     return converted_list
#
# def get_numbers(lines):
#     total_numbers = list()
#     regex = r"\d|one|two|three|four|five|six|seven|eight|nine"
#     for line in lines:
#         match = re.findall(regex, line)
#         if match:
#             match = convert_to_int(match)
#             if len(match) > 1:
#                 first_and_last = match[::len(match) - 1]
#                 final_number = int("".join(map(str, first_and_last)))
#             else:
#                 #final_number = concat(match[0], match[0])
#                 final_number = match[0]
#             total_numbers.append(final_number)
#     return total_numbers


if __name__ == '__main__':
    file = 'input.txt'
    lines = read_file(file)
    totals = get_numbers(lines)
    print(f"{sum(totals)} is the calibration number")
