def printPermutations(s):
    nums = list(s)
    prefix = []
    result = []

    def recursive(prefix, nums):
        if len(nums) == 0:
            result.append(prefix)

        for i in range(len(nums)):
            recursive(prefix + [nums[i]], nums[:i]+nums[i+1:])

    recursive(prefix, nums)
    return result


print(printPermutations("aca"))
