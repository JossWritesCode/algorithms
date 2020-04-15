#!/usr/bin/python

# import argparse


def find_max_profit(prices):
    max_profit = -prices[0] + prices[1]

    i = len(prices) - 1
    max_profit = -prices[-2] + prices[-1]
    while i > 0:
        j = i - 1
        while j >= 0:
            profit = prices[i] + -prices[j]
            if profit > max_profit:
                max_profit = profit
            j -= 1
        i -= 1

    return max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]), "should be 3530")

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
