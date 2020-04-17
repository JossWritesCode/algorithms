#!/usr/bin/python

import sys


def making_change(amount, denominations=[1, 5]):
    if amount < 5 and amount >= 1:
        return 1
    if amount >= 5 and amount < 10:
        return 2
    else:
        return making_change(amount - 1) + making_change(amount - 5)


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
