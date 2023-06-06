# Not Accepted due to time limit - N^3

def fourSum(arr, target):

    arr.sort()  # Sorting the array in ascending order

    for i in range(len(arr)):
        # Skipping duplicate elements for the first number
        if i > 0 and arr[i] == arr[i-1]:
            continue

        for j in range(i+1, len(arr)):
            # Skipping duplicate elements for the second number
            if j > i+1 and arr[j] == arr[j-1]:
                continue

            k = j + 1  # Pointer for the third number
            l = len(arr) - 1  # Pointer for the fourth number

            while k < l:
                # Calculating the sum of the quadruplet
                sum = arr[i] + arr[j] + arr[k] + arr[l]

                if sum < target:  # If the sum is less than the target, move the third pointer forward
                    k += 1
                elif sum > target:  # If the sum is greater than the target, move the fourth pointer backward
                    l -= 1
                else:  # If the sum is equal to the target, a quadruplet exists
                    return "Yes"

    return "No"  # No quadruplet found
