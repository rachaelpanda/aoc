#!/usr/bin/env python3

import math
import pprint
pp = pprint.PrettyPrinter(indent=4)


def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def concat_sequential_keys(digit_dict):
    list_to_join = list()
    joined_num_list = list()
    for line in digit_dict.keys():
        for i in range(0, 142):
            if i in digit_dict[line]:
                # check if index before or after is defined
                if (i - 1) in digit_dict[line] or (i + 1) in digit_dict[line]:
                    list_to_join.append(digit_dict[line][i])
                else:
                    joined_num_list.append(digit_dict[line][i])
            else:
                if list_to_join:
                    joined_nums_string = ''.join(list_to_join)
                    joined_num_list.append(joined_nums_string)
                    list_to_join = list()
    joined_num_list = list(map(int, joined_num_list))
    return joined_num_list


def right_checkity_check(digit_dict, character_dict, line_count, char_index):
    # check line above if possible, current line, and line below if possible
    for line_index in range((line_count - 1), (line_count + 2)):
        if line_index in character_dict:
            # check sequentially left to right
            if line_index == line_count:
                count = 1
            else:
                count = 0
            while 42:
                index = char_index + count
                # check if this index is defined and if it's a digit:
                if index in character_dict[line_index]:
                    character_to_check = character_dict[line_index][index]
                    if character_to_check.isdigit():
                        digit_dict[line_index].update({index: character_to_check})
                # if line above or below, we need to check one more time
                elif line_index != line_count and count == 0:
                    count += 1
                    continue
                else:
                    break
                # decrement for next sequential check
                count += 1
    return digit_dict



def left_checkity_check(digit_dict, character_dict, line_count, char_index):
    # check line above if possible, current line, and line below if possible
    for line_index in range((line_count - 1), (line_count + 2)):
        if line_index not in digit_dict and line_index in character_dict:
                digit_dict[line_index] = dict()
        if line_index in character_dict:
            # check sequentially from right to left of index - 1 always
            count = -1
            while 42:
                index = char_index + count
                # check if this index is defined and if it's a digit:
                if index in character_dict[line_index]:
                    character_to_check = character_dict[line_index][index]
                    if character_to_check.isdigit():
                        digit_dict[line_index].update({index: character_to_check})
                else:
                    break
                # decrement for next sequential check
                count = count - 1
    return digit_dict


def part_two_ig(character_dict):
    part_two_digit_dict = dict()
    pt_two_gears_list = list()
    for line_count in character_dict:
        for char_index in character_dict[line_count].keys():
            if character_dict[line_count][char_index] == '*':
                part_two_digit_dict = left_checkity_check(part_two_digit_dict, character_dict, line_count, char_index)
                part_two_digit_dict = right_checkity_check(part_two_digit_dict, character_dict, line_count, char_index)
                # now that we found out all the things, we need to math it out somehow
                pt_two_joined_num_list = concat_sequential_keys(part_two_digit_dict)
                if len(pt_two_joined_num_list) > 1:
                    result = math.prod(pt_two_joined_num_list)
                    pt_two_gears_list.append(result)
                part_two_digit_dict = dict()
    return pt_two_gears_list

def unhinged_elves(character_dict):
    part_one_digit_dict = dict()
    for line_count in character_dict:
        for char_index in character_dict[line_count].keys():
            if not character_dict[line_count][char_index].isdigit():
                part_one_digit_dict = left_checkity_check(part_one_digit_dict, character_dict, line_count, char_index)
                part_one_digit_dict = right_checkity_check(part_one_digit_dict, character_dict, line_count, char_index)
    return part_one_digit_dict


def remove_periods(lines):
    count = 0
    character_dict = dict()
    for line in lines:
        line = list(line)
        character_dict[count] = dict()
        for index, char in enumerate(line):
            if char != '.':
                character_dict[count].update({index: char})
        count += 1
    return character_dict


if __name__ == '__main__':
    file = 'input.txt'
    lines = read_file(file)
    character_dict = remove_periods(lines)
    part_one_digit_dict = unhinged_elves(character_dict)
    pt_one_joined_num_list = concat_sequential_keys(part_one_digit_dict)
    print(f"Sum of the matching numbers in schematic: {sum(pt_one_joined_num_list)}")
    pt_two_gears_list = part_two_ig(character_dict)
    print(f"Sum of the gears: {sum(pt_two_gears_list)}")
