def printPermutations(s):
    arr = list(s)
    ans = []

    def recursion(index, arr):
        if index == len(arr):
            ans.append(''.join(arr))
            return

        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i], arr[index]
            recursion(index + 1, arr)
            # Backtrack, restore original state
            arr[index], arr[i] = arr[i], arr[index]

    recursion(0, arr)
    return ans


print(printPermutations("abc"))
