def LongestSubsetWithZeroSum(arr):
    # Check if the array is empty
    if not arr:
        return 0

    # Create a dictionary to store the cumulative sum as the key and the index as the value
    mapp = {}

    # Initialize variables for the total sum, length of the longest subset, and current length
    total = 0
    length = 0

    # Iterate over each element in the array
    for i in range(len(arr)):
        # Calculate the cumulative sum by adding the current element to the total
        total += arr[i]

        # Check if the total sum is zero, indicating a subset with zero sum
        if total == 0:
            # Update the dictionary with the element and its index
            mapp[arr[i]] = i
            # Update the length of the longest subset if necessary
            length = max(i+1, length)

        # Check if the total sum is already present in the dictionary
        if total in mapp:
            # Update the length of the longest subset if necessary
            length = max(i - mapp[total], length)

        else:
            # Add the total sum and its index to the dictionary
            mapp[total] = i

    # Return the length of the longest subset with zero sum
    return length


arr = [4, 2, -3, 1, 6]
print(LongestSubsetWithZeroSum(arr))
# Expected output: 2
