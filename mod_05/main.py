#! /usr/bin/env python
"""Sample code to read in test cases:"""
import sys

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            numbers = make_number_list(test)
            cycle = find_cycle(numbers)
            print(make_string(cycle))


def make_number_list(line):
    numbers = []
    for n in line.split():
        numbers.append(int(n))
    
    return numbers
    
def find_cycle(numbers):
    # since we are supposed to find the longest cycle possible from start, not just the first
    # repeating range with 2 elements, we store the cycles we find while expanding the range 
    # end to search for. This means that end was "furthest" away from start when the last
    # cycle was stored
    for start in range(0, len(numbers)):
        for end in range(start+1, len(numbers)):
            range_count = end - start
            s_tail = end
            e_tail = s_tail + range_count
            if numbers[start:end] == numbers[s_tail:e_tail]:
                return numbers[start:end]
                
    return []

def make_string(numbers):
    return(' '.join([str(n) for n in numbers]))

if __name__ == "__main__":
    main()
