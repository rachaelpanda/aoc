#!/usr/bin/env python

from collections import Counter

def get_data(data_file):
    """Grab the data from text file and clean it up"""
    with open(data_file) as f:
        line = f.read()
    lines = line.split(',')
    return lines


def find_fish_count(fish_count, days):
    """For the number of days passed, determine the reproduction rate of our fishies"""
    for day in range(days):
        tomorrow_fish = dict()
        for index in range(9):
            index_str = str(index)
            if index_str not in tomorrow_fish:
                tomorrow_fish[index_str] = 0
            # if fish count is greater than 1, decrement the day for those fish
            if fish_count[index_str] > 0:
                # if we're at day 0, add number of fish to day 8 and day 6 for tomorrow
                if index == 0:
                    tomorrow_fish['6'] = fish_count[index_str]
                    tomorrow_fish['8'] = fish_count[index_str]
                else:
                    decrement_day = index-1
                    decrement_day_str = str(decrement_day)
                    tomorrow_fish[decrement_day_str] = tomorrow_fish[decrement_day_str] + fish_count[index_str]
        # update our fish count default dictionary with tomorrow's fish
        fish_count = tomorrow_fish
    return fish_count


if __name__ == '__main__':
    data_file = 'fishy.txt'
    day_count_down = 80
    diagnostics = get_data(data_file)
    orig_fish_count = Counter(diagnostics)
    current_fish_count = find_fish_count(orig_fish_count, day_count_down)
    print(sum(current_fish_count.values()))
