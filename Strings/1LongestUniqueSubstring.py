from os import *
from sys import *
from collections import *
from math import *


def uniqueSubstrings(input):
    # Two pointer approach
    # Optimizing time to N instead of 2N

    mapp = {}  # To store the index of the last occurrence of each character
    right = 0  # Right pointer
    left = 0   # Left pointer
    length = 0  # Length of the longest substring with most different characters

    while right < len(input):
        if input[right] not in mapp:  # If the character is encountered for the first time
            mapp[input[right]] = right  # Store the index of the character
            length = max(length, right - left + 1)  # Update the length
            right += 1

        else:  # If the character is already present in the map
            # Update the left pointer to skip the previous occurrence
            left = max(left, mapp[input[right]] + 1)
            mapp[input[right]] = right  # Update the index of the character
            length = max(length, right - left + 1)  # Update the length
            right += 1

    return length


# Test Cases
# Expected output: 3, Longest substring with most different characters: "abc"
print(uniqueSubstrings("aabccbb"))
# Expected output: 2, Longest substring with most different characters: "ab"
print(uniqueSubstrings("abbbb"))
# Expected output: 6, Longest substring with most different characters: "abcdef"
print(uniqueSubstrings("abcdef"))
# Expected output: 3, Longest substring with most different characters: "cde"
print(uniqueSubstrings("abccde"))
