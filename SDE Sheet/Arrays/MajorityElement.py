# Moore's Voting Algorithm
# O(N) + O(N)

def findMajorityElement(arr, n):
    count = 0
    element = None

    for i in range(len(arr)):
        if count == 0:
            element = arr[i]
            count = 1
            continue

        if arr[i] == element:
            count += 1
        else:
            count -= 1

    count = 0
    for i in range(len(arr)):
        if element == arr[i]:
            count += 1

    if count > n//2:
        return element

    else:
        return -1


print(findMajorityElement([2, 2, 1, 1, 1, 2, 2], 7))
