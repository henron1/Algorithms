#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_price_now = None
  max_profit = None
  for i in range(len(prices)):
    current_price = prices[i]
    if min_price_now:
      if current_price > min_price_now:
        max_profit = current_price - min_price_now
      else:
        min_price_now = current_price
    else:
      min_price_now = current_price
  return max_profit
# print(find_max_profit([10, 7, 5, 8, 11, 9]))
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

  # print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))