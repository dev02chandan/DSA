def pairSum(arr, s):
    mapp = {}
    ans = []
    for i in range(len(arr)):
        if (s-arr[i]) in mapp:
            ans.append([s-arr[i], arr[i]])
        else:
            mapp[arr[i]] = i
    # ans.reverse()
    return ans


print(
    pairSum([2, -3, 3, 3, -2], 0))
