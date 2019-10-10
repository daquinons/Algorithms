#!/usr/bin/python

import sys
import itertools


def rock_paper_scissors(n):
    options = ["rock", "paper", "scissors"]
    solution = [list(option)
                for option in list(itertools.product(options, repeat=n))]
    return solution


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
