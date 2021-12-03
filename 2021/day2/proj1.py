#!/usr/bin/env python

import re


def get_directions(directions_file):
    """Grab the directions from text file and clean it up"""
    with open(directions_file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def determine_location(directions, whorizontal=0, vertical=0):
    """From our start horizontal and vertical locations, determine where we end up from our directions"""
    for movement in directions:
        direction, units = movement.split(' ')
        units = int(units)
        # increase whorizontal movement upon match
        if re.match(r'forward', direction):
            whorizontal += units
        # increase depth upon match
        elif re.match(r'down', direction):
            vertical += units
        # decrease depth upon match
        elif re.match(r'up', direction):
            vertical -= units
    return whorizontal, vertical


def print_product(a, b):
    """Print the product of two numbers"""
    product = a * b
    print(product)


if __name__ == '__main__':
    directions_file = 'directions.txt'
    directions = get_directions(directions_file)
    whorizontal, vertical = determine_location(directions)
    print_product(whorizontal, vertical)
