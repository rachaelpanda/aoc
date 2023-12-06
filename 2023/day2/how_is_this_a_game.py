#!/usr/bin/env python3

import re

def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def your_dad(game):
    regex_game = r'\d+'
    match = re.search(regex_game, game)
    return int(match[0])


def your_granny(min_of_ea_color, num, color):
    if int(num) > min_of_ea_color[color]:
        min_of_ea_color[color] = int(num)
    return min_of_ea_color


def your_sister(rounds_list):
    total_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    possible = None
    impossible = None
    min_of_ea_color = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for round in rounds_list:
        match = re.findall(r'\d+? green|\d+? blue|\d+? red', round)
        for thingy in match:
            num, color = thingy.split(' ')
            if int(num) <= total_cubes[color]:
                possible = 'yup'
            else:
                impossible = 'yup'
                possible = 'nope'
            min_of_ea_color = your_granny(min_of_ea_color, num, color)
    return possible, impossible, min_of_ea_color


def your_mom(lines):
    total_possible_games = list()
    total_power_of_rounds = list()
    for line in lines:
        game, rounds = line.split(':')
        game = your_dad(game)
        rounds_list = rounds.split(';')
        possible, impossible, min_of_ea_color = your_sister(rounds_list)
        if impossible is None:
            total_possible_games.append(game)
        ans = 1
        for value in min_of_ea_color.values():
            ans = ans * value
        total_power_of_rounds.append(ans)
    return total_possible_games, total_power_of_rounds


if __name__ == '__main__':
    file = 'input.txt'
    lines = read_file(file)
    total_possible_games, total_power_rounds = your_mom(lines)
    print(f"{sum(total_possible_games)}")
    print(f"{sum(total_power_of_rounds)}")
