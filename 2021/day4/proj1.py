#!/usr/bin/env python

import itertools


def get_data(data_file):
    """Grab the data from text file and clean it up"""
    with open(data_file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def create_boards_and_nums(data):
    """Parse our input from file. The first line is the bingo numbers drawn. There is an empty newline separating each
    board"""
    # first line is the bingo numbers drawn
    bingo_nums = [int(i) for i in data[0].split(",")]
    # every line after 2 is a new board, boards are separated by an empty string
    boards = list()
    board_count = -1
    for line in data[1:]:
        if not line:
            board_count += 1
            boards.append([])
        else:
            boards[board_count].append([int(str_num) for str_num in line.split()])
    return bingo_nums, boards


def lets_play(bingo_nums, boards):
    """Using the bingo numbers and the list of our boards, loop through the bingo numbers until we find a winner."""
    drawn_nums = list()
    for num in bingo_nums:
        drawn_nums.append(num)
        for board in boards:
            for row, column in zip(board, list(zip(*board))):
                if all(row_num in drawn_nums for row_num in row) or all(col_num in drawn_nums for col_num in column):
                    return drawn_nums, board, num


def find_all_unmatched_nums(drawn_nums, board):
    """Collect the numbers from the board that were not drawn and find the sum of them."""
    unmatched_nums = list()
    for row in board:
        unmatched_nums.append(list(set(row).difference(drawn_nums)))
    unmatched_nums = list(itertools.chain.from_iterable(unmatched_nums))
    return sum(unmatched_nums)


def print_product(a, b):
    """Print the product of two numbers"""
    product = a * b
    print(product)


if __name__ == '__main__':
    data_file = 'bingo.txt'
    data = get_data(data_file)
    bingo_nums, boards = create_boards_and_nums(data)
    drawn_nums, board, winning_num = lets_play(bingo_nums, boards)
    sum_unmatched_nums = find_all_unmatched_nums(drawn_nums, board)
    print_product(winning_num, sum_unmatched_nums)
