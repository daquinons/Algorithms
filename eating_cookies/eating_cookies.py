#!/usr/bin/python

import sys
import itertools

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    possible_choices = [0, 1, 2, 3]
    successful_choices = []
    for possibility in itertools.combinations_with_replacement(possible_choices, n):
        possibility_without_zeroes = [n for n in possibility if n > 0]
        if sum(possibility_without_zeroes) == n and possibility_without_zeroes not in successful_choices:
            successful_choices.append(possibility_without_zeroes)

    for choice in successful_choices:
        for permutation in itertools.permutations(choice):
            if list(permutation) not in successful_choices:
                successful_choices.append(list(permutation))

    return len(successful_choices)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
