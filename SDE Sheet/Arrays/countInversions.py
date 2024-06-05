def merge(arr1, arr2):
    count = 0
    left = 0
    right = 0
    merged = []
    while (left != len(arr1) and right != len(arr2)):
        # Left is smaller
        if arr1[left] <= arr2[right]:
            merged.append(arr1[left])
            left += 1

        # right is smaller
        else:
            merged.append(arr2[right])
            count += len(arr1[left:])
            right += 1
    merged += arr1[left:]
    merged += arr2[right:]
    return merged, count


def mergeSort(arr):

    count = 0

    if len(arr) <= 1:
        return arr, count

    mid = len(arr)//2

    # Sort the first half - low to mid
    left, count_left = mergeSort(arr[:mid])

    # Sort the second half - mid+1 to high
    right, count_right = mergeSort(arr[mid:])

    final, count_merge = merge(left, right)

    count = count + count_left + count_right + count_merge

    return final, count


def countInversions(arr):
    final, count = mergeSort(arr)
    return count


print(countInversions([5, 3, 2, 4, 1]))
