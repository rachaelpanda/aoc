#!/usr/bin/env python3


def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def get_overlap(lines):
    contain_count = 0
    overlap_count = 0
    for line in lines:
        numbers = [int(num) for elf in line.split(',') for num in elf.split('-')]
        elf_range1 = [int(num) for num in range(numbers[0], numbers[1] + 1)]
        elf_range2 = [int(num) for num in range(numbers[2], numbers[3] + 1)]
        if all(elem in elf_range1 for elem in elf_range2) or all(elem in elf_range2 for elem in elf_range1):
            contain_count += 1
        for num in elf_range1:
            if num in elf_range2:
                overlap_count += 1
                break
    return contain_count, overlap_count


if __name__ == '__main__':
    file = 'puzzle_input.txt'
    lines = read_file(file)
    contain_count, overlap_count = get_overlap(lines)
    print(f'{contain_count}')
    print(f'{overlap_count}')

