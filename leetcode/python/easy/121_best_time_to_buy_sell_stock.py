"""
Say you have an array for which the ith element is the price of a given stock on
day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.
"""


def max_profit(prices):
    max_price = 0
    diff = 0
    for price in reversed(prices):
        max_price = max(price, max_price)
        prev_diff = diff
        diff = max_price - price

        if diff < prev_diff:
            diff = prev_diff

    return diff


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))

prices = [7, 6, 4, 3, 1]
print(max_profit(prices))

prices = [2, 1, 2, 1, 0, 1, 2]
print(max_profit(prices))
