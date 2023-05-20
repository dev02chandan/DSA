def maxSubarraySum(arr, n):
    sum = 0
    max = float('-inf')
    for i in range(n):
        sum += arr[i]
        if max < sum:
            max = sum

        if sum < 0:
            sum = 0
    if max < 0:
        max = 0
    return max


print(maxSubarraySum([1, 2, 7, -4, 3, 2, -10, 9, 1], 9))
