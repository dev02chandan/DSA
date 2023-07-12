# def kthPermutation(n, k):
#     nums = list(range(1, n + 1))
#     prefix = []
#     result = []

#     def permute(prefix, nums):
#         if len(nums) == 0:
#             result.append(''.join(map(str, prefix)))
#             return

#         for i in range(len(nums)):
#             permute(prefix + [nums[i]], nums[:i] + nums[i + 1:])

#     permute(prefix, nums)
#     return result[k-1]


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        ans = ""
        nums = []

        # Calculate the factorial and initialize the list of numbers
        for i in range(1, n + 1):
            nums.append(i)
            fact *= i

        k = k - 1
        fact = fact // n

        def getPermutationsHelper(nums, k, fact):
            # Base case: If there is only one number remaining, return it as a string
            if len(nums) == 1:
                return str(nums[0])

            # Calculate the index of the digit to select and update k
            index = k // fact
            k = k % fact

            # Select the digit at the calculated index and remove it from the list
            digit = str(nums[index])
            nums.pop(index)

            # Update the factorial based on the reduced list length
            fact = fact // len(nums)

            # Recursively find the permutations for the remaining digits
            return digit + getPermutationsHelper(nums, k, fact)

        return getPermutationsHelper(nums, k, fact)


# Test Case
solution = Solution()
n = 3
k = 3
# Expected output: "213"
print(solution.getPermutation(n, k))

# Approach:
# - To find the kth permutation of numbers from 1 to n, we can use a recursive approach.
# - We first calculate the factorial of n to determine the total number of permutations.
# - We subtract 1 from k since the permutation numbering starts from 1.
# - We divide the factorial by n to get the factorial of (n-1).
# - Then, we use a helper function to find the kth permutation recursively.
# - In each recursion, we calculate the index of the digit to select based on the quotient of k divided by the factorial.
# - We update k to the remainder of k divided by the factorial.
# - We remove the selected digit from the list and reduce the factorial by dividing it by the length of the remaining list.
# - We concatenate the selected digit with the result of the recursive call for the remaining digits.
# - Finally, we return the final permutation.
# - The time complexity of this approach is O(n^2) due to the recursive calls and list manipulations.
# - The space complexity is O(n) for the list of numbers and the recursive call stack.
