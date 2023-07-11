from typing import List


def combinationSum2(arr: List[int], n: int, target: int) -> List[List[int]]:
    ans = []  # List to store the combinations that sum to target
    ds = []  # List to track the current combination
    arr.sort()  # Sort the input array to handle duplicates and maintain ascending order

    def findCombinations(index, value):
        # Base case: Combination sum equals target
        if value == target:
            ans.append(ds[:])
            return

        # Iterate through the remaining elements starting from the current index
        for i in range(index, len(arr)):

            # Skip duplicates to avoid duplicate combinations
            if i != index and arr[i] == arr[i-1]:
                continue

            # Optimization: Skip elements that are greater than the remaining target value
            if arr[i] > target - value:
                break

            # Add the current element to the combination
            ds.append(arr[i])
            # Recursively search for combinations with the remaining elements
            findCombinations(i + 1, value + arr[i])
            # Backtrack by removing the current element from the combination
            ds.pop()

    # Start the recursive search from index 0 with initial value 0
    findCombinations(0, 0)

    # Sort the combinations in lexicographical order
    ans.sort(key=lambda x: (x, len(x)))

    return ans


# Test Cases
arr1 = [10, 1, 2, 7, 6, 1, 5]
n1 = len(arr1)
target1 = 8
# Expected output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
print(combinationSum2(arr1, n1, target1))

arr2 = [2, 5, 2, 1, 2]
n2 = len(arr2)
target2 = 5
# Expected output: [[1, 2, 2], [5]]
print(combinationSum2(arr2, n2, target2))

arr3 = [1, 2, 3]
n3 = len(arr3)
target3 = 4
# Expected output: [[1, 3]]
print(combinationSum2(arr3, n3, target3))


'''

Approach:

Sort the input array in ascending order to handle duplicates and maintain consistency in the combinations.
Use a recursive function to find combinations that sum to the target.
Start the recursive function with an initial index of 0 and value of 0.
Iterate through the remaining elements, skipping duplicates to avoid duplicate combinations.
Perform an optimization by skipping elements that are greater than the remaining target value, as they cannot contribute to valid combinations.
Add the current element to the combination, recursively search for combinations with the remaining elements, and backtrack by removing the current element.
Store the valid combinations in the ans list.
Sort the combinations in lexicographical order using a custom key function that considers both the elements and the length of each combination.
Return the sorted combinations.
Time Complexity: The time complexity of this approach is O(2^N), where N is the length of the input array. This is because each element in the array can either be included or excluded in a combination, leading to a total of 2^N possible combinations.

Space Complexity: The space complexity is O(N), where N is the length of the input array. This is due to the space required to store the combinations and the recursive function call stack.

'''
