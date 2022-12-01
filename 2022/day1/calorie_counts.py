#!/usr/bin/env python3


def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def get_totals(lines):
    count = 0
    totals = list()
    for line in lines:
        if line:
            count = count + int(line)
        else:
            totals.append(count)
            # reset values
            count = 0
    return totals


if __name__ == '__main__':
    file = 'puzzle_input.txt'
    lines = read_file(file)
    totals = get_totals(lines)
    totals.sort(reverse=True)
    most_calories = totals[0]
    print(f"{most_calories} is highest calorie count")
    top_three = totals[0] + totals[1] + totals[2]
    print(f"{top_three} is top three calorie count")


