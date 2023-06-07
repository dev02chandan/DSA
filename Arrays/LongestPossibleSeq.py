

def lengthOfLongestConsecutiveSequence(arr, n):
    # Check if the array is empty
    if not arr:
        return 0

    # Create a set from the array to efficiently check for existence of elements
    myset = set(arr)

    # Initialize variables for counting the consecutive sequence
    count = 1
    max_count = 1

    # Iterate over each element in the array
    for i in arr:
        # Check if the previous element (i-1) is not in the set, indicating the start of a consecutive sequence
        if i-1 not in myset:
            num = int(i)
            # Keep incrementing the number and counting until the consecutive sequence ends
            while (True):
                # Check if the next number (num+1) is present in the set
                if int(num+1) in myset:
                    count += 1
                    num += 1
                else:
                    # Update the maximum count if necessary and reset the count for the next sequence
                    max_count = max(count, max_count)
                    count = 1
                    break

    # Return the maximum count of consecutive elements
    return max_count


arr = [100, 4, 200, 1, 3, 2]
n = len(arr)
result = lengthOfLongestConsecutiveSequence(arr, n)
print(f"The length of the longest consecutive sequence in {arr} is: {result}")
# Expected output: The length of the longest consecutive sequence in [100, 4, 200, 1, 3, 2] is: 4
