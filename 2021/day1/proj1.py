#!/usr/bin/env python


def get_depth_readings(depth_file):
    """Grab the sonar readings from text file and clean it up"""
    with open(depth_file) as f:
        lines = f.readlines()
    lines = [int(line.strip()) for line in lines]
    return lines


def get_depth_increase_count(depth_list):
    """Count the number of times depth has increased"""
    count = 0
    previous_depth = None
    for index, depth in enumerate(depth_list):
        if index == 0:
            # Do nothing
            pass
        else:
            if depth > previous_depth:
                count += 1
        # Set depth for next comparison
        previous_depth = depth
    return count


if __name__ == '__main__':
    depth_file = 'sonar_depth.txt'
    depth_list = get_depth_readings(depth_file)
    count = get_depth_increase_count(depth_list)
    print(count)
