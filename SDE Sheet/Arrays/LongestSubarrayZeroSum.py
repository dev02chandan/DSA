def longestSubarrayWithSumK(a, k: int) -> int:
    total = a[0]           # Variable to track the sum of the subarray
    maxi = 0               # Variable to store the maximum length of subarray with sum k
    i = 0                  # Pointer for the start index of the subarray
    j = 0                  # Pointer for the end index of the subarray

    while i < len(a) and j < len(a):
        if total == k:                        # If the current subarray sum is equal to k
            # Update the maximum length if necessary
            maxi = max(j - i + 1, maxi)
            j += 1                            # Move the end pointer to the right
            if j < len(a):
                # Add the next element to the subarray sum
                total += a[j]
        elif total < k or i == j:              # If the subarray sum is less than k or the subarray has only one element
            j += 1                            # Move the end pointer to the right
            if j < len(a):
                # Add the next element to the subarray sum
                total += a[j]
        else:                                 # If the subarray sum is greater than k
            # Subtract the element at the start index from the subarray sum
            total -= a[i]
            i += 1                            # Move the start pointer to the right

    # Return the maximum length of the subarray with sum k
    return maxi


# Test Cases
arr = [1, 2, 3, 4, 5]
k = 9
print(longestSubarrayWithSumK(arr, k))  # Expected output: 2

arr = [3, 1, 4, 2, 1, 2, 1, 3, 2]
k = 6
print(longestSubarrayWithSumK(arr, k))  # Expected output: 4

arr = [1, 2, 3, 4, 5]
k = 15
print(longestSubarrayWithSumK(arr, k))  # Expected output: 5

arr = [-1, -2, -3, -4, -5]
k = -8
print(longestSubarrayWithSumK(arr, k))  # Expected output: 3

arr = [2, 4, 6, 8, 10]
k = 5
print(longestSubarrayWithSumK(arr, k))  # Expected output: 0
