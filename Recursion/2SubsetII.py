from os import *
from sys import *
from collections import *
from math import *

from typing import *


def uniqueSubsets(n: int, arr: List[int]) -> List[List[int]]:
    """
    Approach:
    1. Sort the array to handle duplicates efficiently.
    2. Use a recursive approach to generate all unique subsets.
    3. At each step, add the current subset to the result list.
    4. Recurse by including the next element (if it's not a duplicate) and excluding it.
    5. Pop the last element from the current subset after each recursive call.
    6. Return the final result list.
    """

    ans = []
    arr.sort()
    ds = []

    def findSubsets(index):
        # Add a copy of the current subset to the result list
        ans.append(ds[:])

        for i in range(index, len(arr)):
            if i != index and arr[i] == arr[i - 1]:
                continue  # Skip duplicates to avoid generating duplicate subsets

            ds.append(arr[i])
            findSubsets(i + 1)  # Recurse by including the next element
            ds.pop()  # Pop the last element to backtrack and try the next element

    findSubsets(0)

    return ans


# Testcases
n = 3
arr = [1, 2, 3]
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(uniqueSubsets(n, arr))

n = 3
arr = [1, 1, 2]
# Output: [[], [1], [1, 1], [1, 1, 2], [1, 2], [2]]
print(uniqueSubsets(n, arr))

n = 4
arr = [1, 2, 2, 3]
# Output: [[], [1], [1, 2], [1, 2, 2], [1, 2, 2, 3], [1, 2, 3], [2], [2, 2], [2, 2, 3], [2, 3], [3]]
print(uniqueSubsets(n, arr))


# Time complexity: O(2^n), where n is the number of elements in the given list
# Space complexity: O(2^n), as the result list can have a maximum of 2^n subsets


'''
Recursion Tree
                            []
             /                          \
            [1]                         []
       /          \                /          \
    [1, 2]         [1]         [2]           []
   /      \       /    \      /    \       /    \
[1, 2, 3] [1, 2] [1, 3] [1] [2, 3] [2]  [3]     []

'''

'''
Dry Run

uniqueSubsets(0, [])
    |
    +-- uniqueSubsets(1, [1])
    |       |
    |       +-- uniqueSubsets(2, [1, 2])
    |       |       |
    |       |       +-- uniqueSubsets(3, [1, 2, 2])  <-- [1, 2, 2] is added to ans
    |       |
    |       +-- uniqueSubsets(3, [1])  <-- [1] is added to ans
    |
    +-- uniqueSubsets(2, [])
    |       |
    |       +-- uniqueSubsets(3, [2])
    |       |       |
    |       |       +-- uniqueSubsets(4, [2, 3])  <-- [2, 3] is added to ans
    |       |
    |       +-- uniqueSubsets(4, [2])  <-- [2] is added to ans
    |
    +-- uniqueSubsets(3, [])
    |       |
    |       +-- uniqueSubsets(4, [2])
    |       |       |
    |       |       +-- uniqueSubsets(5, [2, 3])  <-- [2, 3] is added to ans
    |       |
    |       +-- uniqueSubsets(5, [3])  <-- [3] is added to ans
    |
    +-- uniqueSubsets(4, [])
    |       |
    |       +-- uniqueSubsets(5, [3])  <-- [3] is added to ans
    |
    +-- uniqueSubsets(5, [])  <-- [] is added to ans

'''
