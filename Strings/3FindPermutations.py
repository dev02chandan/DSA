def printPermutations(s):
    arr = list(s)
    ans = []

    def recursion(index, arr):
        # Base case: If all characters are fixed, append the current permutation to the result
        if index == len(arr):
            ans.append(''.join(arr))
            return

        # Try swapping each character with the current index and recursively generate permutations
        for i in range(index, len(arr)):
            # Swap characters
            arr[index], arr[i] = arr[i], arr[index]
            # Recurse to generate permutations for the next index
            recursion(index + 1, arr)
            # Backtrack, restore original state
            arr[index], arr[i] = arr[i], arr[index]

    recursion(0, arr)
    return ans


# Test Case
print(printPermutations("abc"))
# Expected output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# Approach:
# - The function uses a recursive approach to generate all permutations of a given string.
# - It converts the string into a list of characters to facilitate swapping.
# - The function uses a helper recursive function, `recursion`, that takes an index and the list of characters.
# - In each recursive call, the function fixes one character at a time by swapping it with the current index.
# - After swapping, it recurses to the next index and continues generating permutations.
# - At the base case, when the index reaches the end of the list, it appends the current permutation to the result.
# - The function backtracks by swapping the characters back to the original state before returning from each recursive call.
# - The time complexity of this approach is O(n!), where n is the length of the string, as it generates all possible permutations.
# - The space complexity is also O(n!) to store the resulting permutations.
