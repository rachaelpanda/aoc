!/usr/bin/env python3


def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def crates(lines):
    crates = dict()
    count = 1
    for i in range(9):
        line = lines[i]

        crates[count] =
    return crates


if __name__ == '__main__':
    file = 'puzzle_input.txt'
    lines = read_file(file)