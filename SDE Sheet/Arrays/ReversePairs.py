def countPairs(arr, low, mid, high):
    count = 0
    right = mid + 1
    for i in range(low, mid+1):
        while (right <= high and arr[i] > 2*arr[right]):
            right += 1
        count += (right-(mid+1))

    return count


def merge(arr, low, mid, high):
    left = low
    right = mid+1

    temp = []

    while (left <= mid and right <= high):
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while (left <= mid):
        temp.append(arr[left])
        left += 1

    while (right <= high):
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp[i - low]


def mergeSort(arr, low, high):

    count = 0

    if low == high:
        return count

    mid = (low+high)//2

    count += mergeSort(arr, low, mid)

    count += mergeSort(arr, mid+1, high)

    count += countPairs(arr, low, mid, high)

    merge(arr, low, mid, high)

    return count


def reversePairs(arr, n):
    return mergeSort(arr, 0, n-1)


print(reversePairs([2, 4, 3, 5, 1], 5))
