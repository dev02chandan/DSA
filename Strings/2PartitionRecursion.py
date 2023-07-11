from typing import List


def partition(string: str) -> List[List[str]]:
    ans = []  # List to store the palindrome partitions
    ds = []  # List to track the current partition

    def isPalindrome(string: str, start: int, end: int) -> bool:
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True

    def findPartition(string: str, index: int):
        if index == len(string):
            ans.append(ds[:])
            return

        for i in range(index, len(string)):
            if isPalindrome(string, index, i):
                ds.append(string[index:i+1])
                findPartition(string, i+1)
                ds.pop()

    findPartition(string, 0)

    return ans


# Test Case
string = "aab"
# Expected output: [['a', 'a', 'b'], ['aa', 'b']]
print(partition(string))


# Approach:
# - Use a recursive function to find all possible palindrome partitions of the given string.
# - Start the recursive function with an initial index of 0 and an empty partition list 'ds'.
# - Iterate through the string and check if each substring from the current index to the end is a palindrome.
# - If a palindrome is found, add it to the partition list 'ds', and recursively find the partitions for the remaining substring.
# - Backtrack by removing the last added palindrome from the partition list to explore other possibilities.
# - Once the index reaches the end of the string, add the current partition list to the result list 'ans'.
# - Return the 'ans' list containing all possible palindrome partitions.

# Time Complexity: The time complexity of this approach is O(N * 2^N), where N is the length of the string.
#                  This is because there can be 2^N possible partitions, and for each partition, checking if it is a palindrome takes O(N) time.
# Space Complexity: The space complexity is O(N), where N is the length of the string. This is due to the space required to store the partitions and the recursive function call stack.
