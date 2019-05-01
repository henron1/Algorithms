#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxProfit = 0 #setting intial maximum profit
  for i in range(0, len(prices)): #looping over outer scope of prices
    for j in range(i + 1, len(prices)): #inner scope of prices that is 1 ahead of the outer scope price
      profit = prices[j] - prices[i] #setting up remainder of profit
      print(profit) 
      if maxProfit == 0: # if there's no max profit then it is set to the previous remainder
        maxProfit = profit
      elif profit > maxProfit: # if there's no max profit then swap
        # swap = profit
        # maxProfit = swap
        profit, maxProfit = maxProfit, profit
  return maxProfit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))