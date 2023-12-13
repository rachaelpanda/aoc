#!/usr/bin/env python3


def read_file(file):
    """open file and return list of lines"""
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def total_scratch_cards(cards_dict):
    count = 0
    for card in cards_dict:
        count += cards_dict[card]['copy_count']
    return count


def idk(cards_dict):
    points = list()
    for card in cards_dict.keys():
        count = 0
        for check in cards_dict[card]['check']:
            if check in cards_dict[card]['winning']:
                if count:
                    count += count
                else:
                    count = 1
                # pt 2
                cards_dict[card]['match_count'] += 1
        if count:
            points.append(count)
        # pt 2
        for i in range(card + 1, card + cards_dict[card]['match_count'] + 1):
            cards_dict[i]['copy_count'] += cards_dict[card]['copy_count']
    return points, cards_dict


def get_numbers_lists(numbers):
    winning, list_to_check = numbers.split('|')
    winning = winning.split(' ')
    list_to_check = list_to_check.split(' ')
    winning = [int(i) for i in winning if i.isdigit()]
    list_to_check = [int(i) for i in list_to_check if i.isdigit()]
    return winning, list_to_check


def get_card_number(line):
    card, numbers = line.split(':')
    card = card.split(' ')
    card_num = [i for i in card if i.isdigit()]
    return int(card_num[0]), numbers


def make_it_pretty(lines):
    cards_dict = dict()
    for line in lines:
        card_num, numbers = get_card_number(line)
        winning, list_to_check = get_numbers_lists(numbers)
        # add counts for pt 2
        cards_dict[card_num] = {'copy_count': 1, 'match_count': 0, 'winning': winning, 'check': list_to_check}
    return cards_dict


if __name__ == '__main__':
    file = 'input.txt'
    lines = read_file(file)
    cards_dict = make_it_pretty(lines)
    points, cards_dict = idk(cards_dict)
    print(f'Total points: {sum(points)}')
    # pt 2
    card_count = total_scratch_cards(cards_dict)
    print(f'Total scratch cards: {card_count}')

