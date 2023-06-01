"""
Problem Statement:
Given an integer array 'arr', find all the elements that appear more than ⌊n/3⌋ times in the array.
Note: The algorithm should run in linear time and in O(1) space.

Approach:
We can apply the Boyer-Moore Voting Algorithm to solve this problem.
The algorithm works by selecting two elements, which are the majority elements if they exist.
We iterate through the array and update the counts for the selected elements.
At the end, we verify the counts to determine if they are greater than ⌊n/3⌋, and if so, add them to the result.

"""


def majorityElementII(arr):
    target = len(arr) // 3

    el1 = None
    count1 = 0

    el2 = None
    count2 = 0

    # Select potential majority elements
    for i in range(len(arr)):
        if count1 == 0 and arr[i] != el2:
            el1 = arr[i]
            count1 += 1

        elif count2 == 0 and arr[i] != el1:
            el2 = arr[i]
            count2 += 1

        elif arr[i] == el1:
            count1 += 1

        elif arr[i] == el2:
            count2 += 1

        else:
            count1 -= 1
            count2 -= 1

    # Check for element 1 and element 2 counts
    count1 = 0
    count2 = 0

    for i in range(len(arr)):
        if arr[i] == el1:
            count1 += 1

        if arr[i] == el2:
            count2 += 1

    ans = []
    # Add elements to the result if their counts are greater than the target
    if count1 > target:
        ans.append(el1)

    if count2 > target:
        ans.append(el2)

    return ans


print(majorityElementII([2, 1, 1, 3, 1, 4, 5, 6]))
