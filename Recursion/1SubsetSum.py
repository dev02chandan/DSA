from sys import *
from collections import *
from math import *

from typing import List


def subsetSum(num: List[int]) -> List[int]:
    """
    Approach:
    1. Use a recursive approach to generate all possible subsets of the given numbers.
    2. At each step, we have two choices: include the current number or exclude it.
    3. Generate all subsets by recursively calling the solution function with the next index and updated value.
    4. Append the value to the result array at each leaf node.
    5. Sort the result array in ascending order and return it.
    """

    if not num:
        return None

    arr = []

    def solution(index, value):
        # Base Case
        if index == len(num):
            arr.append(value)
            return

        solution(index + 1, value + num[index])
        solution(index + 1, value)

    solution(0, 0)

    arr.sort()

    return arr


# Testcases
nums = [1, 2, 3]
print(subsetSum(nums))  # Output: [0, 1, 2, 3, 4, 5, 6]

nums = [4, 5, 6]
print(subsetSum(nums))  # Output: [0, 4, 5, 6, 9, 10, 11, 15]

nums = [10, 20]
print(subsetSum(nums))  # Output: [0, 10, 20, 30]


# Time complexity: O(2^n), where n is the number of elements in the given list
# Space complexity: O(2^n), as the result array can have a maximum of 2^n elements
