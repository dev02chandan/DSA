def merge(arr1, arr2):
    left = 0
    right = 0
    merged = []
    while (left != len(arr1) and right != len(arr2)):
        if arr1[left] <= arr2[right]:
            merged.append(arr1[left])
            left += 1
        else:
            merged.append(arr2[right])
            right += 1
    merged += arr1[left:]
    merged += arr2[right:]
    return merged


def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    # Sort the first half - low to mid
    left = mergeSort(arr[:mid])

    # Sort the second half - mid+1 to high
    right = mergeSort(arr[mid:])

    return merge(left, right)


print(mergeSort([10, 5, 2, 7, 9, 3, 1, 8, 6, 4]))
