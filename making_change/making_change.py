#!/usr/bin/python

import sys
import itertools


def making_change(amount, denominations):
    solutions = []
    denominations.sort()
    if 0 not in denominations:
        denominations.insert(0, 0)
    for option in itertools.combinations_with_replacement(denominations, amount):
        sum_option = sum(option)
        if sum_option == amount:
            solutions.append(list(option))

    return len(solutions)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
