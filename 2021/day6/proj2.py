#!/usr/bin/env python

from collections import Counter

import proj1


if __name__ == '__main__':
    data_file = 'fishy.txt'
    day_count_down = 256
    diagnostics = proj1.get_data(data_file)
    orig_fish_count = Counter(diagnostics)
    current_fish_count = proj1.find_fish_count(orig_fish_count, day_count_down)
    print(sum(current_fish_count.values()))
