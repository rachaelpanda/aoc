#!/usr/bin/env python

import re

import proj1


def determine_location(directions, whorizontal=0, vertical=0, aim=0):
    """From our start horizontal and vertical locations, determine where we end up from our directions"""
    for movement in directions:
        direction, units = movement.split(' ')
        units = int(units)
        # increase whorizontal movement upon match
        # and multiply aim by units to determine increase to vertical depth
        # add increased depth to total depth
        if re.match(r'forward', direction):
            whorizontal += units
            if aim > 0:
                depth_increase = aim * units
                vertical += depth_increase
        # increase aim upon match
        elif re.match(r'down', direction):
            aim += units
        # decrease aim upon match
        elif re.match(r'up', direction):
            aim -= units
    return whorizontal, vertical


if __name__ == '__main__':
    directions_file = 'directions.txt'
    directions = proj1.get_directions(directions_file)
    whorizontal, vertical = determine_location(directions)
    proj1.print_product(whorizontal, vertical)
