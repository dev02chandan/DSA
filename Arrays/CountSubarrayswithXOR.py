from math import *
from collections import *
from sys import *
from os import *


def subarraysXor(arr, x):
    """
    Count the number of subarrays in 'arr' that have XOR equal to 'x'.

    Args:
        arr (list): Input array of integers.
        x (int): XOR value.

    Returns:
        int: Count of subarrays with XOR equal to 'x'.
    """

    hashmap = {}  # Hashmap to store XOR values and their counts
    count = 0  # Initialize the count of subarrays
    xr = 0  # Initialize the XOR value

    hashmap[0] = 1  # Initial value (0 XOR anything = anything)

    for i in range(len(arr)):
        xr = xr ^ arr[i]  # Calculate the XOR with the current element

        if xr ^ x in hashmap:
            # Increment count if XOR value matches 'x'
            count += hashmap[xr ^ x]

        if xr in hashmap:
            hashmap[xr] += 1  # Increment the count of XOR value in the hashmap

        else:
            hashmap[xr] = 1  # Add the XOR value to the hashmap with count 1

    return count


# Test Cases
arr1 = [4, 2, 2, 6, 4]
x1 = 6
# Subarrays with XOR 6: [4, 2], [2, 2, 6], [6], [6, 4]
# Expected output: 4

arr2 = [5, 6, 7, 8, 9]
x2 = 5
# Subarrays with XOR 5: [5], [5, 6, 7, 8, 9]
# Expected output: 2

arr3 = [1, 1, 1, 1, 1]
x3 = 2
# Subarrays with XOR 2: []
# Expected output: 0

# Call the function and print the results
print(subarraysXor(arr1, x1))  # Output: 4
print(subarraysXor(arr2, x2))  # Output: 2
print(subarraysXor(arr3, x3))  # Output: 0
