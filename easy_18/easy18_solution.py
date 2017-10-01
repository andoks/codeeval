#! /usr/bin/env python3
"""Sample code to read in test cases:"""

import sys

def parse(line: str) -> (int, int):
    target, multipler = line.split(",")

    return (int(target), int(multipler))

def find_smallest_multippel_greater_than(target: int, multipler: int) -> int:
    result = multipler
    while result < target:
        result += multipler

    return result

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            target, multipler = parse(line)
            smallest_greater_multiple = find_smallest_multippel_greater_than(target, multipler)
            print(smallest_greater_multiple)

