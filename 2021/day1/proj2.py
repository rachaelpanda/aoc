#!/usr/bin/env python

from collections import deque

import proj1


def get_sum_depth(depth_list, n=3):
    count = 0
    # Create our deque object with first 3 elements in the depth list with the max length of 3
    d = deque(depth_list[:3], n)
    previous_sum = sum(d)
    # skipping the first 3 elements, loop through depth list and get the sum of our deque object
    # until we no longer have 3 elements in it
    for depth in depth_list[3:]:
        d.append(depth)
        if len(d) == 3:
            current_sum = sum(d)
            if current_sum > previous_sum:
                count += 1
            previous_sum = current_sum
    return count


if __name__ == '__main__':
    depth_file = 'sonar_depth.txt'
    depth_list = proj1.get_depth_readings(depth_file)
    count = get_sum_depth(depth_list)
    print(count)

