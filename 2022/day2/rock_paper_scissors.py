#!/usr/bin/env python3


def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def get_first_totals(lines):
    count = 0
    legend = {
        'A' : 1, # rock
        'B' : 2, # paper
        'C' : 3, # scissors
        'X' : 1, # rock
        'Y' : 2, # paper
        'Z' : 3 # scissors
    }
    lose = 0
    draw = 3
    win = 6
    for line in lines:
        opponent_play, your_play = line.split(' ')
        if legend[opponent_play] == legend[your_play]:
            # draw
            count += draw
            count += legend[your_play]
        elif legend[opponent_play] == 1 and legend[your_play] == 3:
            # lose
            count += lose
            count += legend[your_play]
        elif legend[your_play] == 1 and legend[opponent_play] == 3:
            # win
            count += win
            count += legend[your_play]
        elif legend[your_play] > legend[opponent_play]:
            # win
            count += win
            count += legend[your_play]
        else:
            # lose
            count += lose
            count += legend[your_play]
    return count


def get_second_totals(lines):
    count = 0
    legend = {
        'A' : 1, # rock
        'B' : 2, # paper
        'C' : 3, # scissors
        'X' : 0, # lose
        'Y' : 3, # draw
        'Z' : 6 # win
    }
    rock = 1
    paper = 2
    scissors = 3
    for line in lines:
        opponent_play, outcome = line.split(' ')
        if legend[outcome] == 3:
            # draw
            count += legend[opponent_play]
            count += legend[outcome]
        elif legend[outcome] == 0:
            # lose
            if legend[opponent_play] == 1:
                your_play = scissors
            else:
                # max points again
                your_play = legend[opponent_play]
                your_play -= 1
            count += your_play
            count += legend[outcome]
        else:
            # win
            if legend[opponent_play] == 3:
                your_play = rock
            else:
                # i tried for max points
                your_play = legend[opponent_play]
                your_play += 1
            count += your_play
            count += legend[outcome]
    return count



if __name__ == '__main__':
    file = 'puzzle_input.txt'
    lines = read_file(file)
    count = get_first_totals(lines)
    print(f'{count}')
    second_count = get_second_totals(lines)
    print(f'{second_count}')
