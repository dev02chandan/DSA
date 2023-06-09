from os import *
from sys import *
from collections import *
from math import *


def uniqueSubstrings(input):

    # Two pointer approach

    myset = set()  # Set to store unique characters
    right = 0  # Right pointer
    left = 0  # Left pointer
    length = 0  # Length of current substring

    while (right < len(input)):

        if input[right] not in myset:
            myset.add(input[right])  # Add current character to the set
            # Update the length if needed
            length = max(length, right - left + 1)
            right += 1  # Move the right pointer

        else:
            while (input[left] != input[right]):
                # Remove characters until the first occurrence of the current character
                myset.discard(input[left])
                left += 1  # Move the left pointer

            # Remove the first occurrence of the current character
            myset.discard(input[left])
            left += 1  # Move the left pointer

            myset.add(input[right])  # Add current character to the set
            right += 1  # Move the right pointer

    return length


# Test Cases:

# Case 1:
input1 = "abacabad"  # Input string
# Expected output: 3
# Explanation: The unique substrings are "aba", "bac", and "bad".
print(uniqueSubstrings(input1))

# Case 2:
input2 = "abcdabcd"  # Input string
# Expected output: 4
# Explanation: The unique substrings are "abcd", "bcda", "cdab", and "dabc".
print(uniqueSubstrings(input2))

# Case 3:
input3 = "aaaaa"  # Input string
# Expected output: 1
# Explanation: All characters are the same, so the only unique substring is the whole string.
print(uniqueSubstrings(input3))
