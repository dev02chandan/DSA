from os import *
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    """
    Approach:
    1. Start from the largest denomination and check if it can be used to form the remaining amount.
    2. Keep subtracting the largest denomination from the amount until it becomes zero.
    3. Repeat the process with the next largest denomination.
    4. Count the number of denominations used to form the amount and return the count.
    """

    index = None
    for i in range(len(denominations) - 1, -1, -1):
        if amount / denominations[i] >= 1:
            index = i
            break

    ans = 0
    while amount != 0:
        if amount < denominations[index]:
            index -= 1
            continue
        amount -= denominations[index]
        ans += 1

    return ans


# Testcases
amount = 43
print(findMinimumCoins(amount))  # Output: 5

amount = 87
print(findMinimumCoins(amount))  # Output: 7

amount = 1256
print(findMinimumCoins(amount))  # Output: 6


# Time complexity: O(n), where n is the number of denominations
# Space complexity: O(1)
