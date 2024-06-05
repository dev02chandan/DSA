

def triplet(n: int, arr):
    ans = []  # List to store the triplets

    arr.sort()  # Sorting the array in ascending order

    for i in range(n):
        # Skipping duplicate elements to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue

        j = i + 1  # Pointer for the second element
        k = n - 1  # Pointer for the third element

        while j < k:
            # Calculating the sum of the triplet
            sum = arr[i] + arr[j] + arr[k]

            if sum < 0:  # If the sum is less than 0, move the second pointer forward
                j += 1
            elif sum > 0:  # If the sum is greater than 0, move the third pointer backward
                k -= 1
            else:  # If the sum is 0, it forms a triplet
                # Adding the triplet to the result list
                ans.append([arr[i], arr[j], arr[k]])
                j += 1  # Moving the second pointer forward
                k -= 1  # Moving the third pointer backward

                # Skipping duplicate elements to avoid duplicate triplets
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1

    return ans  # Returning the list of triplets
