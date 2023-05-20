from os import *
from sys import *
from collections import *
from math import *


def maximumProfit(prices):
    profit = 0
    maxi = -1

    for i in range(len(prices)-2, -1, -1):
        profit += prices[i+1]-prices[i]

        if maxi < profit:
            maxi = profit

        if profit < 0:
            profit = 0

    if maxi < 0:
        maxi = 0
    return maxi
