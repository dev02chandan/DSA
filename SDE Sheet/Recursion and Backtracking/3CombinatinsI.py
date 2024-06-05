from typing import List


def findSubsetsThatSumToK(arr: List[int], n: int, k: int) -> List[List[int]]:
    ans = []  # List to store the subsets that sum to k
    ds = []  # List to track the current subset

    def subset(index: int, val: int, ds: List[int]):
        if val == k and ds not in ans:
            ans.append(ds[:])

        if index == n:
            return

        # Not Pick
        subset(index + 1, val, ds)

        ds.append(arr[index])
        # Pick
        subset(index + 1, val + arr[index], ds)
        ds.pop()

    subset(0, 0, ds)
    ans.sort()
    return ans


# Test Cases
arr1 = [2, 3, 4, 5]
n1 = len(arr1)
k1 = 7
# Expected output: [[2, 5], [3, 4]]
print(findSubsetsThatSumToK(arr1, n1, k1))

arr2 = [1, 2, 3]
n2 = len(arr2)
k2 = 4
# Expected output: [[1, 3]]
print(findSubsetsThatSumToK(arr2, n2, k2))

arr3 = [1, 2, 3, 4]
n3 = len(arr3)
k3 = 10
# Expected output: [[1, 2, 3, 4]]
print(findSubsetsThatSumToK(arr3, n3, k3))


'''
Approach:

Use a recursive function to find subsets that sum to the target value k.
Start the recursive function with an initial index of 0, value of 0, and an empty subset ds.
If the current subset sum equals k and the subset is not already present in the ans list, add the subset to ans.
Iterate through the remaining elements, either by not picking the current element or by picking it and recursively searching for subsets with the remaining elements.
Pop the last element from the subset to backtrack and explore other possibilities.
Sort the subsets in lexicographical order.
Return the sorted subsets.
Time Complexity: The time complexity of this approach is O(2^N), where N is the length of the input array. This is because each element in the array can either be included or excluded in a subset, leading to a total of 2^N possible subsets.

Space Complexity: The space complexity is O(N), where N is the length of the input array. This is due to the space required to store the subsets and the recursive function call stack.
'''
