#!/usr/bin/python

import sys
import itertools

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    possible_choices = [0, 1, 2, 3]
    successful_choices = []
    for possibility in itertools.product(possible_choices, repeat=n):
        possibility_without_zeroes = [n for n in possibility if n > 0]
        if sum(possibility_without_zeroes) == n:
            successful_choices.append(
                "".join([str(number) for number in possibility_without_zeroes]))

    return len(set(successful_choices))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        num_cookies = 3
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
