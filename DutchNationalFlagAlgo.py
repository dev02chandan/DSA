def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def sort012(arr, n):
    low = 0
    mid = 0
    high = n-1

    while (high >= mid):
        if arr[mid] == 0:
            swap(arr, mid, low)
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            swap(arr, mid, high)
            high -= 1

    return arr


print(sort012(
    [0, 1, 2, 2, 1, 0], 6))
