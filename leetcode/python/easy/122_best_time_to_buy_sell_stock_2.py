"""
Say you have an array for which the ith element is the price of a given stock on
day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
"""
import sys


def max_profit(prices):
    profits = []
    upturn = False
    last_valley = sys.maxsize
    prev_price = prices[0] if len(prices) > 0 else None

    for price in prices:
        prev_upturn = upturn

        # if current price is less than previous price and we were previously
        # going up, that means we've found a peak and the trend has reversed.
        if price < prev_price:
            upturn = False

        # if current price is greater than previous price and previously we were
        # going down, then we've found a valley and the trend has reversed.
        if price > prev_price:
            upturn = True

        if prev_upturn and not upturn:
            profits.append(prev_price - last_valley)
        elif upturn and not prev_upturn:
            last_valley = prev_price

        prev_price = price

    if upturn:
        profits.append(prev_price - last_valley)

    return sum(profits)


prices = [2, 1, 2, 0, 1]
print(max_profit(prices))

prices = [7, 6, 4, 3, 1]
print(max_profit(prices))

prices = [2, 1, 2, 1, 0, 1, 2]
print(max_profit(prices))
