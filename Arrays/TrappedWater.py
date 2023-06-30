def getTrappedWater(arr, n):
    """
    Calculates the amount of water that can be trapped given an array of heights.

    Args:
        arr (list): List of integer heights.
        n (int): Length of the array.

    Returns:
        int: Amount of water that can be trapped.

    """

    if n < 3:
        return 0

    left = 0
    right = n - 1

    leftmax = 0
    rightmax = 0

    ans = 0

    # Two-pointer approach to calculate trapped water
    """
    Approach:
    - Use two pointers, one starting from the left side (left) and the other from the right side (right).
    - Initialize two variables, leftmax and rightmax, to keep track of the maximum height encountered on each side.
    - Initialize a variable, ans, to store the trapped water.
    - While the left pointer is less than or equal to the right pointer:
        - If the height at the left pointer is less than or equal to the height at the right pointer:
            - Check if the height at the left pointer is greater than or equal to leftmax:
                - If true, update leftmax.
                - If false, calculate the trapped water by subtracting the height at the left pointer from leftmax and add it to ans.
            - Increment the left pointer.
        - If the height at the left pointer is greater than the height at the right pointer:
            - Check if the height at the right pointer is greater than or equal to rightmax:
                - If true, update rightmax.
                - If false, calculate the trapped water by subtracting the height at the right pointer from rightmax and add it to ans.
            - Decrement the right pointer.
    - Return the calculated ans, which represents the total trapped water.

    Complexity Analysis:
    - The time complexity is O(n) since we iterate through the array once.
    - The space complexity is O(1) since we use constant extra space.

    """

    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= leftmax:
                leftmax = arr[left]
            else:
                ans += leftmax - arr[left]

            left += 1

        else:
            if arr[right] >= rightmax:
                rightmax = arr[right]
            else:
                ans += rightmax - arr[right]

            right -= 1

    return ans


# Testcases

arr = [3, 0, 0, 2, 0, 4]
n = len(arr)
print(getTrappedWater(arr, n))
# Output: 10
# Explanation: Water can be trapped between the heights 0, 2, and 4.

arr = [7, 4, 0, 9]
n = len(arr)
print(getTrappedWater(arr, n))
# Output: 10
# Explanation: Water can be trapped between the heights 4 and 9.

arr = [6, 9, 9]
n = len(arr)
print(getTrappedWater(arr, n))
# Output: 0
# Explanation: No water can be trapped as there are no lower heights.

arr = [1, 2, 3, 4, 5]
n = len(arr)
print(getTrappedWater(arr, n))
# Output: 0
# Explanation: No water can be trapped as the heights are increasing.

arr = []
n = len(arr)
print(getTrappedWater(arr, n))
# Output: 0
# Explanation: No water can be trapped in an empty array.
