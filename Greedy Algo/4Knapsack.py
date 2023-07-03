from os import *
from sys import *
from collections import *
from math import *


def maximumValue(items, n, w):
    """
    Approach:
    - Sort the items list based on the ratio of value/weight in descending order.
    - Iterate through the sorted items list and greedily select items as long as the weight limit is not exceeded.
    - If the weight of the next item exceeds the remaining weight limit, take a fraction of it to maximize the value.
    - Return the maximum value achieved.
    """

    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    weight = 0
    value = 0
    i = 0

    while (i < n):
        if (items[i][0] + weight) <= w:
            value += items[i][1]
            weight += items[i][0]
            i += 1
        else:
            value += items[i][1] * (w - weight) / items[i][0]
            break

    return value


# Test cases
items = [[10, 60], [20, 100], [30, 120]]
n = len(items)
w = 50
# Expected output: 240
print(maximumValue(items, n, w))

items = [[5, 50], [10, 60], [20, 140]]
n = len(items)
w = 30
# Expected output: 220
print(maximumValue(items, n, w))

# Time complexity: O(n log n), where n is the number of items
# Space complexity: O(1)
