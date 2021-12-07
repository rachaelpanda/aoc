#!/usr/bin/env python

import proj1


def check_if_won(board, drawn_nums):
    for row, column in zip(board, list(zip(*board))):
        if all(row_num in drawn_nums for row_num in row) or all(col_num in drawn_nums for col_num in column):
            return True
    return False

def find_last_matched_board(bingo_nums, boards):
    """Using the bingo numbers and the list of our boards, loop through the bingo numbers until we find a the last
    winning board."""
    drawn_nums = list()
    matched_boards = list()
    num = 0
    for num in bingo_nums:
        drawn_nums.append(num)
        if len(boards) == 1 and check_if_won(boards[0], drawn_nums):
            return boards[0], num, drawn_nums
        boards = [board for board in boards if not check_if_won(board, drawn_nums)]
    return False


if __name__ == '__main__':
    data_file = 'bingo.txt'
    data = proj1.get_data(data_file)
    bingo_nums, boards = proj1.create_boards_and_nums(data)
    last_board, winning_num, drawn_nums = find_last_matched_board(bingo_nums, boards)
    sum_unmatched_nums = proj1.find_all_unmatched_nums(drawn_nums, last_board)
    proj1.print_product(winning_num, sum_unmatched_nums)