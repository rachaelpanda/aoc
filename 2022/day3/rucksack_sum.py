#!/usr/bin/env python3

import re
import string

def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def get_duplicate_characters(lines):
    dupes = list()
    for line in lines:
        compartment1, compartment2 = line[:len(line) // 2], line[len(line) // 2:]
        for char in compartment1:
            if re.search(char, compartment2):
                dupes.append(char)
                break
    return dupes


def get_char_values():
    count = 1
    values = dict()
    for char in string.ascii_letters:
        values[char] = count
        count += 1
    return values


def get_some(dupes, char_values):
    some_got_get = 0
    for char in dupes:
        some_got_get += char_values[char]
    return some_got_get


def get_badge_chars(lines):
    elf_rucksack_list = list()
    badges = list()
    for line in lines:
        elf_rucksack_list.append(line)
        if len(elf_rucksack_list) == 3:
            for char in elf_rucksack_list[0]:
                if re.search(char, elf_rucksack_list[0]) and re.search(char, elf_rucksack_list[1]) and re.search(char, elf_rucksack_list[2]):
                    badges.append(char)
                    elf_rucksack_list = list()
                    break
    return badges


if __name__ == '__main__':
    file = 'puzzle_input.txt'
    lines = read_file(file)
    dupes = get_duplicate_characters(lines)
    char_values = get_char_values()
    sum = get_some(dupes, char_values)
    print(f'{sum}')
    badges = get_badge_chars(lines)
    sum2 = get_some(badges, char_values)
    print(f'{sum2}')

